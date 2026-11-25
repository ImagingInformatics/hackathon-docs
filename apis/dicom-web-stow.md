# Push DICOM to STOW
Pushing DICOM files at a web archive takes a little more effort, but is still made easy by simple off-the-shelf tools. [cURL](https://curl.se/) is one of these. It is a command line tool built for almost every platform that knows how to talk "web".

For example, to upload a single part 10 DICOM file to the hackathon server's STOW-RS endpoint, just use cURL like this:

```bash
curl -X POST -H "apikey: [MyApiKey]" -H "Content-Type: multipart/related; type=application/dicom" -F "file=@[dicom.dcm];type=application/dicom" "https://hackathon.siim.org/dicomweb/studies" -v
```

Replace the parts in square brackets with the appropriate value, i.e.:

* **[MyApiKey]** - your SIIM Hackathon API key (the one you got after signing the participant agreement)
* **[dicom.dcm]** - the DICOM file name you want to send. You can also send multiple DICOM files at once by repeating the `-F "file=@..."` part.

Anything you upload is deleted by the daily reset at 3:00 AM US Eastern, so keep your own copy.
