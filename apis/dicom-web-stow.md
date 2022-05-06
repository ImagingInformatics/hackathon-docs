# Push DICOM to STOW
Pushing DICOM files at a web archive takes a little more effort, but is still made easy by simple off-the-shelf tools. [cURL](http://curl.haxx.se/) is one of these. It is a command line tool built for almost every platform that knows how to talk "web".

For example, to upload a single part 10 DICOM file to one of the STOW enabled hackathon archives, just use cURL like this:

```curl -X POST -H "APIKey: [MyApiKey]" -H "Content-Type: multipart/related; type=application/dicom" -F "file=@[dicom.dcm];type=application/dicom" "http://hackathon.siim.org/dicomweb/studies" -v```

Replace the parts in red with the appropriate value, i.e.:

* **[MyApiKey]** - your SIIM Hackathon API Key for the API Gateway (the one you got after signing the participation agreement)
* **[dicom.dcm]** with the DICOM file name you want to send. You can also send multiple DICOM files at once by repeating that underlined segment.
