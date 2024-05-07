# How To Convert DICOM To JPG or PNG

## Introduction
DICOM is a container, which combines a header (metadata like patient ID, study date, etc) with pixel data (i.e. the image itself). The latter may be uncompressed data (i.e. bitmap) or could be compressed into one of the many codecs suported by the DICOM standard, such as JPEG-LS, JPEG 2000 and more recently High-Throughput JPEG 2000 (HTJ2K). Sometimes it is easier to extract the pixel data into a simple JPG or PNG file to work with the images, and how to do so is described in this article via two methods: 1) DICOMweb and 2) Command-line utilities. You could also achieve the same things via code/scripting using a DICOM library but that's out of scope for this article.

*Note:* do remember that DICOM may not always contain pixel data. There are types of DICOM objects which are purley metadata-based like Structured Reports (SR) and Key-Object Selection (KOS) as two examples.

### 1. Extracting JPG/PNG Via DICOMweb
Check your server's DICOM conformance statement to ensure it supports the `/rendered` call in WADO-RS. See the [DICOM standard](https://www.dicomstandard.org/using/dicomweb/retrieve-wado-rs-and-wado-uri) for more details. We use [Orthanc](https://www.orthanc-server.com/) and know that it supports this call.

If your server supports this endpoint, then the rest is easy! You can just set a `GET` call using the following URL format (replace the UIDs in curly brackets with the values you're working with):
```
/studies/{Study Instance UID}/series/{Series Instance UID}/instances/{SOP Instance UID}/rendered
```
and add an `Accept` header with either `image/jpeg` or `image/png` depending on what you want, and that should be all!

#### DICOMweb Example
Here's a working example from the [SIIM Hackathon Server](../getting-started/hackathon-server.md). It required a valid hackathon API key:

```
https://hackathon.siim.org/dicomweb/studies/1.3.6.1.4.1.14519.5.2.1.6279.6001.300027087262813745730072134723/series/1.3.6.1.4.1.14519.5.2.1.6279.6001.513114548408601984123939083099/instances/1.3.6.1.4.1.14519.5.2.1.6279.6001.197993217821785409800235232773/rendered
```
By default, Orthanc returns a JPEG image, but you can change that with:
```
Accept: image/png
```
You can try this via tools like [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/), etc.

### 2. Extracting JPG/PNG Via Command-Line Interface (CLI) Utilities
For this, we'll be using the excellent [dcm4che CLI toolkit](https://web.dcm4che.org/dcm4che-utilities). This toolkit works on Windows, Mac and Linux (even headless servers). You can download the latest and greatest verion of dcm4che [here](https://sourceforge.net/projects/dcm4che/files/dcm4che3/) (you'll want to download the file ending with `-bin.zip`).

Once downloaded, you can run `dcm2jpg` and point it to a DICOM file to export the pixel data like so:
```
./dcm4che-5.23.2/bin/dcm2jpg /path/to/dicom-file.dcm
```

Find more information on dcm2jpg [here](https://github.com/dcm4che/dcm4che/blob/master/dcm4che-tool/dcm4che-tool-dcm2jpg/README.md) or by running `dcm2jpg --help`

#### CLI Example
Assuming you have both dcm4che and this [sample hackathon image](https://github.com/ImagingInformatics/hackathon-images/blob/master/Ravi%20SIIM/W_Chest_PA_3172/IM-0031-0001.dcm) downloaded to the current folder (and dcm4che unzipped). You can run the following to export to JPEG:
```
./dcm4che-5.23.2/bin/dcm2jpg IM-0031-0001.dcm IM-0031-0001.jpg
```
Or, the following to go with PNG instead:
```
./dcm4che-5.23.2/bin/dcm2jpg -F PNG IM-0031-0001.dcm IM-0031-0001.jpg
```