# Before we start...
If you have not signed the participant agreement yet, that would be the first thing you should do - [Hackathon Agreement](https://siim.org/learning-events/events/hackathon/siim-hackathon-api-platform-participant-agreement/). Once you have the signed the agreement, an email will be sent to you with your API key.

Secondly, don't forget to join the conversation on [Slack](https://join.slack.com/t/siimhackathon/shared_invite/zt-mkk0yn2e-KUqOLi6ETBUQmOffxmcQxA). Keep an eye on the different [hackathon events](https://siim.org/page/hacking_healthcare) as listed on the website to get the most out of it.

## New to REST APIs?
Wondering what's all this hype about the new standards - check our [5-minute starting guide for FHIR](../apis/fhir-intro.md) as well as [starting guide for DICOMweb](../apis/dicom-web-intro.md). You won't believe how easy and quick it is to get started!

# Using the SIIM Hackathon Server

When making requests against the end points below, ensure you include an HTTP header like so:

```apikey: [your API key]```

We recommend using [Postman](https://www.postman.com/) for working with RESTful APIs, such as FHIR and DICOMweb. You can use Postman to get your API calls working, then Postman can export into code in your favourite language (Python, Javascript, etc.)


## FHIR: 
* Endpoint: 
    * R5: `https://hackathon.siim.org/fhir/`
    * R4: `https://hackathon.siim.org/fhir-r4/`
* Overview of FHIR objects/resources at: [https://hackathon.siim.org/](https://hackathon.siim.org/) (requires [browser plugin](./mod-header.md)). This is only available for R5.
* Server powered by [HAPI FHIR](http://hapifhir.io/)

## DICOMweb: 
* Endpoint: `https://hackathon.siim.org/dicomweb/`
* WADO-URI endpoint: `https://hackathon.siim.org/wadouri/`
* VNA Web UI at [https://hackathon.siim.org/vna/](https://hackathon.siim.org/vna/)  (requires [browser plugin](./mod-header.md))
* Server powered by [Orthanc DICOM Server](http://www.orthanc-server.com/)

## IHE SOLE: 
* Endpoint: `https://hackathon.siim.org/sole/`
* Check out the [Profile text](https://wiki.ihe.net/index.php/Standardized_Operational_Log_of_Events_(SOLE)) and [Github project](https://github.com/mohannadhussain/ihe-sole-repo) for information on how to use the API and event submission samples.

### Notes
* The server resets itself every day at 3am Eastern Time. The process can take up to 10 minutes where some services and/or data may not be available.

## See also
* [Resources of Interest](../apis/other-apis-and-standards.md) - other APIs, Libraries, etc.
* [Datasets](../miscellaneous/data-sets.md) - Openly available datasets in medical imaging.

**Tip**: If your prefer testing right from within your browser, you can use an extension like [ModHeader](./mod-header.md) to send your API key via HTTP headers.
