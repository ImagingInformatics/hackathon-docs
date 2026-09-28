# 5-Minute DICOMweb Starting Guide

## DICOMweb Concepts
To get started with DICOMweb, there are a few key concepts to understand.
* An imaging structure consists of a Patient (typically corresponds to a single "person"), a Study (typically corresponds to a single "diagnostic order"), a Series (typically corresponds to a single "imaging event" within a study, for example, multiple views, or with/without contrast), and an Instance (typically corresponds to a single image).
* First, you must QUERY for studies and their underlying structure, using the QIDO-RS feature of DICOMweb.
* Then, you can RETRIEVE individual instances for rendering, using the WADO-RS feature of DICOMweb.
* If desired, you can STORE individual instances, using the STOW-RS feature of DICOMweb.

## Prerequisites
1. [SIIM Hackathon API key](../getting-started/hackathon-server.md)
2. (Optional) [Postman](https://www.postman.com/)

### Don't forget...
When making requests against the end points below, ensure you include an HTTP header like so: 
`apikey: [your API key]`

If you don't have a SIIM Hackathon API key, see [Hackathon Server](../getting-started/hackathon-server.md).

## 1. A Hello World example
A simple Hello World type query for DICOMweb, would look as follows, to query for all studies for all patients with the last name of **SIIM**: 

```https://hackathon.siim.org/dicomweb/studies/?00100010=SIIM*```
 
**NOTE:** If you having trouble formulating a QIDO request, an alternative way to discover patients/studies is to use Orthanc's web UI at: [https://hackathon.siim.org/vna/](https://hackathon.siim.org/vna/)


## 2. Get study information
Once you've picked a study to download, extract the study UID from the response and you can download its study structure by making a subsequent QIDO-RS query: 

```https://hackathon.siim.org/dicomweb/studies/1.3.6.1.4.1.14519.5.2.1.4792.2001.103189108764313019491934667255/instances```

## 3. Switch return format between XML and JSON
If you want to control the format of the server response, add an `Accept` header with `application/json` for JSON or `text/xml` for XML.

**NOTE:** When you choose XML, DICOMweb returns results in `multipart` format, which is used to combine multiple objects into one response. Read more about multipart at [here](https://pspdfkit.com/blog/2021/a-brief-tour-of-multipart-requests/) and [here](https://swagger.io/docs/specification/describing-request-body/multipart-requests/).

## 4. Download DICOM Images
And once you've done that, select an image to download from the response, extract the series UID and instance UID from the response and you can download the **DICOM** image by making a subsequent WADO-RS query: 

```https://hackathon.siim.org/dicomweb/studies/1.3.6.1.4.1.14519.5.2.1.4792.2001.103189108764313019491934667255/series/1.3.6.1.4.1.14519.5.2.1.4792.2001.104616474240757574154876423123/instances/1.3.6.1.4.1.14519.5.2.1.4792.2001.267212981954448819074140522716```
 
Ensure your request includes a header that specifies the return type, i.e.

`Accept: application/dicom`

## 5. View Images in JPEG/PNG

Add `/frames/1/rendered` to the URL from the last step, and change your `Accept` header to either `image/jpeg` or `image/png`. Here's the full URL:

```http://hackathon.siim.org/dicomweb/studies/1.3.6.1.4.1.14519.5.2.1.7777.9002.198875685720513246512710453733/series/1.3.6.1.4.1.14519.5.2.1.7777.9002.207203214132667549392101803048/instances/1.3.6.1.4.1.14519.5.2.1.7777.9002.327873213718058651550666129029/frames/1/rendered```

## 6. Using WADO-URL instead of WADO-RS
If you are working with a server that does not support DICOMweb, you can retrieve images (as DICOM, or rendered JPEG/PNG) using the older WADO-URL standard. For example:

```https://hackathon.siim.org/wadouri/?requestType=WADO&studyUID=1.3.6.1.4.1.14519.5.2.1.4792.2001.103189108764313019491934667255&seriesUID=1.3.6.1.4.1.14519.5.2.1.4792.2001.104616474240757574154876423123&objectUID=1.3.6.1.4.1.14519.5.2.1.4792.2001.267212981954448819074140522716```
 
The URL above returns DICOM. If you want a rendered JPEG or PND, simply add `&contentType=image/jpeg` or `&contentType=image/png` to your **URL** (not header) request.

## Would you like to see some sample code?
Who wouldn't? Right?!?

With cURL:

```bash
curl -H "apikey: YOUR_API_KEY" \
     -H "Accept: application/dicom+json" \
     "https://hackathon.siim.org/dicomweb/studies/?00100010=SIIM*"
```

With Python, using [requests](https://pypi.org/project/requests/):

```python
import requests

BASE = "https://hackathon.siim.org/dicomweb"
HEADERS = {"apikey": "YOUR_API_KEY", "Accept": "application/dicom+json"}

# 1. Find studies for the SIIM demo patients (QIDO-RS)
studies = requests.get(
    f"{BASE}/studies/", params={"00100010": "SIIM*"}, headers=HEADERS, timeout=30
).json()

for study in studies:
    study_uid = study["0020000D"]["Value"][0]          # StudyInstanceUID
    name = study.get("00100010", {}).get("Value", [{}])[0].get("Alphabetic", "")
    print(study_uid, name)

# 2. Download the DICOM instances of the first study (WADO-RS)
if studies:
    first_uid = studies[0]["0020000D"]["Value"][0]
    response = requests.get(
        f"{BASE}/studies/{first_uid}",
        headers={"apikey": "YOUR_API_KEY", "Accept": "multipart/related; type=application/dicom"},
        timeout=120,
    )
    print(response.status_code, len(response.content), "bytes")
```

If you get a `403`, check that the `apikey` header is present and correct.

## Beyond simple viewing
Interested in pushing data to the server? [This article](./dicom-web-stow.md) provides tips on how to do that using cURL, which can easily be adapted for use with other tools, like Postman.

## Resources
* [DICOMweb documentation](http://www.dicomweb.org/)
* [DICOMweb CheatSheet](https://www.dicomstandard.org/docs/librariesprovider2/dicomdocuments/dicom/wp-content/uploads/2018/04/dicomweb-cheatsheet.pdf)
* [QIDO-RS](ftp://medical.nema.org/medical/dicom/final/sup166_ft5.pdf)
* [WADO-RS](ftp://medical.nema.org/medical/dicom/final/sup161_ft.pdf)
* [STOW-RS](ftp://medical.nema.org/medical/dicom/Final/sup163_ft3.pdf)
