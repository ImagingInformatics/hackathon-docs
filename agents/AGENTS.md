# Project notes for AI coding agents

This project uses the SIIM Hackathon server. Follow the reference below whenever
you write code that calls `hackathon.siim.org`.

<!-- Generated from agents/siim-api.md by agents/build.py. Edit the source, not this file. -->

## SIIM Hackathon API: reference for AI coding agents

This file tells an AI coding agent how to use the SIIM Hackathon server
(`https://hackathon.siim.org`) correctly. It is written for agents first and
people second. The server is shared by every team at the event, so the rules
in "Be a good neighbour" are requirements, not suggestions.

### Authentication

- Every request needs the HTTP header `apikey: <key>`. Header name is lowercase
  `apikey`. There is no OAuth, no bearer token, no query-string key.
- Read the key from the environment variable `SIIM_API_KEY`. Never hard-code it,
  print it, log it, put it in a URL, or commit it. Assume any committed key is
  public within minutes.
- Event keys start with `siimrsna_`. They stop working on **Dec 2, 2026 at
  6:00 PM US Central**. After that every request returns `403`.

### Endpoints

| Service | Base URL | Notes |
| --- | --- | --- |
| FHIR R5 | `https://hackathon.siim.org/fhir/` | HAPI FHIR. Default choice. |
| FHIR R4 | `https://hackathon.siim.org/fhir-r4/` | HAPI FHIR. Use when a library only speaks R4. |
| DICOMweb (QIDO-RS, WADO-RS, STOW-RS) | `https://hackathon.siim.org/dicomweb/` | Orthanc. |
| WADO-URI (legacy) | `https://hackathon.siim.org/wadouri/` | Only if a tool cannot do DICOMweb. |

Use the base URLs exactly as written, including the trailing path. Nothing else
on the host is part of the participant API.

#### Content negotiation

- FHIR: send `Accept: application/fhir+json`.
- DICOMweb queries (QIDO-RS): send `Accept: application/dicom+json`.
- DICOMweb retrieve of DICOM files (WADO-RS): send
  `Accept: multipart/related; type=application/dicom`.
- Rendered images: append `/frames/1/rendered` to an instance URL and send
  `Accept: image/png` or `Accept: image/jpeg`.
- DICOMweb store (STOW-RS): `POST` to `/dicomweb/studies` with
  `Content-Type: multipart/related; type=application/dicom`.

#### Known-good starting queries

```
GET /fhir/Patient?name=SIIM                     # demo patients
GET /fhir/ImagingStudy?patient=siimandy         # studies for one demo patient
GET /dicomweb/studies?00100010=SIIM*            # same patients, DICOM side
GET /dicomweb/studies/{StudyInstanceUID}/series
GET /dicomweb/studies/{StudyInstanceUID}/series/{SeriesInstanceUID}/instances
```

The data is synthetic or de-identified demo data. There is no real patient data
on this server, and you must not upload any.

### Limits

| Limit | Value | What you see when you exceed it |
| --- | --- | --- |
| Requests per key | 15 per second, short bursts up to 40 | `429` with a `Retry-After` header |
| Whole server | Shared cap across all teams | `429` even when you are under your own rate |
| FHIR request body | 10 MB | `413` |
| DICOMweb request body (STOW) | 100 MB per request | `413`; split large studies into several requests |

These limits take effect before the event starts (Nov 29, 2026). Write code that
respects them from the start.

### Status codes and what to do

| Code | Meaning | Correct response |
| --- | --- | --- |
| `200`, `201` | Success | Continue. |
| `403` | Missing, wrong or expired key | Stop. Check `SIIM_API_KEY` is set and sent as the `apikey` header. Do not retry in a loop. |
| `404` | Resource or path not found | Check the base URL and IDs. Do not retry. |
| `413` | Request body too large | Make the request smaller. Do not retry the same request. |
| `429` | Rate limited (your key or the whole server) | Wait the number of seconds in `Retry-After`, then retry. See the client below. |
| `502`, `503`, `504` | Server restarting or overloaded | Wait 30 to 60 seconds and retry a few times, then stop and tell the user. |

### Be a good neighbour

1. Keep at most 4 requests in flight at once. Do not fan out hundreds of
   parallel requests.
2. Honour `Retry-After` on every `429`. Never retry immediately and never retry
   forever.
3. Page through results with `_count` (FHIR) or `limit`/`offset` (QIDO-RS)
   instead of asking for everything. Never crawl the whole server.
4. Cache what you download locally and reuse it. Do not fetch the same study
   twice in one session.
5. Stop and report to the user after repeated `403`, `413` or `5xx` responses
   instead of trying variations.
6. Only use the endpoints in the table above.

### Daily reset

The server resets every day at **3:00 AM US Eastern** and is unavailable for up
to 10 minutes. Anything you uploaded (FHIR resources or DICOM studies) is
deleted by the reset. Keep the source data for anything you upload in your own
project so you can re-upload it.

### Python client with correct retry behaviour

Use this as the starting point for any Python code that calls the server.

```python
import os
import random
import time

import requests

API_KEY = os.environ["SIIM_API_KEY"]          # never hard-code the key
FHIR = "https://hackathon.siim.org/fhir"
DICOMWEB = "https://hackathon.siim.org/dicomweb"

session = requests.Session()
session.headers["apikey"] = API_KEY


def wait_seconds(response, attempt):
    """Seconds to wait before retrying a 429 or 5xx response."""
    jitter = random.uniform(0, 1)            # spread retries so teams don't retry in lockstep
    retry_after = response.headers.get("Retry-After", "")
    if retry_after.isdigit():                # 429: the server says how long to wait
        return int(retry_after) + jitter
    return min(2 ** attempt, 30) + jitter    # 5xx: 2, 4, 8, 16, 30 seconds


def call(method, url, max_attempts=5, **kwargs):
    """Send one request, retrying only on 429 and 5xx."""
    for attempt in range(1, max_attempts + 1):
        response = session.request(method, url, timeout=60, **kwargs)
        if response.status_code == 429 or response.status_code >= 500:
            if attempt == max_attempts:
                break
            time.sleep(wait_seconds(response, attempt))
            continue
        response.raise_for_status()   # 403, 404, 413: do not retry
        return response
    raise RuntimeError(f"{method} {url} still failing after {max_attempts} attempts")


patients = call(
    "GET", f"{FHIR}/Patient",
    params={"name": "SIIM", "_count": 20},
    headers={"Accept": "application/fhir+json"},
).json()
```

### Help

- Ask in the event Slack, channel `#ask-the-mentors`.
- Human-readable docs: https://imaginginformatics.github.io/hackathon-docs/
