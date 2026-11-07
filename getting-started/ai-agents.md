# Using AI Coding Agents (RSNA 2026)

This page is for teams at the RSNA 2026 Vibe Coding Hackathon (Nov 29 to Dec 2, McCormick Place)
who want to build on the SIIM Hackathon server's FHIR and DICOMweb data with an AI coding agent
such as Claude Code, OpenAI Codex, GitHub Copilot or Amazon's agent tools.

It takes about five minutes: get a key, store it safely, drop one instruction file into your
project, and your agent knows how to use the server.

## 1. Get an event API key

Read the [SIIM Hackathon API Platform Participant Agreement](https://siim.org/learning-events/events/hackathon/siim-hackathon-api-platform-participant-agreement/),
then request a key with the [SIIM API key request form](https://docs.google.com/forms/d/e/1FAIpQLSd9tFFjouv2ROqlZ-h9GFtKEb0c9JOGRdNcoMLbCZ8kx9lkig/viewform).
You sign the agreement in the form by typing your full name. You will receive a personal key by
email within one business day. Event keys:

* start with `siimrsna_`
* belong to one person; each teammate who runs an agent should request their own
* stop working on **Dec 2, 2026 at 6:00 PM US Central**

## 2. Store the key in a `.env` file, never in code

In the root of your project, create a file named `.env`:

```bash
SIIM_API_KEY=siimrsna_your_key_here
```

Then make sure git ignores it:

```bash
echo ".env" >> .gitignore
```

Load it in Python with [python-dotenv](https://pypi.org/project/python-dotenv/)
(`from dotenv import load_dotenv; load_dotenv()`), or in Node with
[dotenv](https://www.npmjs.com/package/dotenv). Most agents also read `.env` files directly.

Assume any key that reaches GitHub is public within minutes. If yours leaks, ask in
`#ask-the-mentors` and we will revoke it and issue a new one.

## 3. Give your agent the SIIM instructions

Download one of these files into your project. Both hold the same content: endpoints, the
`apikey` header, limits, status codes, the daily reset, and a Python client that retries correctly.

| Agent | File | Where it goes in your project |
| --- | --- | --- |
| Claude Code | [SKILL.md](https://raw.githubusercontent.com/ImagingInformatics/hackathon-docs/main/agents/SKILL.md) | `.claude/skills/siim-hackathon-api/SKILL.md` |
| OpenAI Codex, GitHub Copilot, and agents that read `AGENTS.md` | [AGENTS.md](https://raw.githubusercontent.com/ImagingInformatics/hackathon-docs/main/agents/AGENTS.md) | `AGENTS.md` in the project root (append to it if you already have one) |
| Any other agent | Either file | Paste it into the agent's project instructions or first prompt |

From a terminal in your project root:

```bash
# Claude Code
mkdir -p .claude/skills/siim-hackathon-api
curl -o .claude/skills/siim-hackathon-api/SKILL.md \
  https://raw.githubusercontent.com/ImagingInformatics/hackathon-docs/main/agents/SKILL.md

# Codex, Copilot and others
curl -o AGENTS.md \
  https://raw.githubusercontent.com/ImagingInformatics/hackathon-docs/main/agents/AGENTS.md
```

## 4. Limits

The server is shared by every team at the event, so each key is rate limited. These limits take
effect before the event starts (Nov 29, 2026).

| Limit | Value |
| --- | --- |
| Requests per key | 15 per second, short bursts up to 40 |
| FHIR upload size | 10 MB per request |
| DICOMweb (STOW) upload size | 100 MB per request |

If your agent gets `429 Too Many Requests`, it is going too fast: it should wait the number of
seconds in the `Retry-After` header and try again. The instruction files tell it to do this.

## 5. Things to know

* The server resets every day at 3:00 AM US Eastern and is down for up to 10 minutes. Anything you
  uploaded is deleted, so keep your source data in your project and re-upload it after a reset.
* All data on the server is synthetic or de-identified. Never upload real patient data.
* Endpoint details and example queries: [Hackathon Server](./hackathon-server.md),
  [FHIR guide](../apis/fhir-intro.md), [DICOMweb guide](../apis/dicom-web-intro.md).

## Help

Ask in the event Slack channel `#ask-the-mentors`, or see the support contact at the bottom of
every page.
