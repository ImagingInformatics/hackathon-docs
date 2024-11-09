# 5-Minute FHIR Starting Guide

## FHIR Concepts
All FHIR calls are based on retrieving resources. There are many different types of resources for data you would like to retrieve, including patient information, orders, reports, results, and more.

## Prerequisites
1. [SIIM Hackathon API key](../getting-started/hackathon-server.md)
2. (Optional) [Postman](https://www.postman.com/)

### Don't forget...
When making requests against the end points below, ensure you include an HTTP header like so: 

`apikey: [your API key]`

If you don't have a SIIM Hackathon API key, see [Hackathon Server](../getting-started/hackathon-server.md).

## 1. A Hello World example
A simple Hello World type query for FHIR, would look as follows, to query for all patients with the last name of **SIIM**: 

``http://hackathon.siim.org/fhir/Patient?name=SIIM``

## 2. Finding "Imaging Studies" of a given patient
Once you've picked a patient to download, extract the patient ID by using the ID field from the response and you can download available studies by making a subsequent ImagingStudy query: 

```http://hackathon.siim.org/fhir/ImagingStudy?patient=siimandy```

## 3. Switch return format between XML and JSON
If you want to control the format of the server response, add an `Accept` header with `application/json` for JSON or `text/xml` for XML.

## Would you like to see some sample code? 
Who wouldn't? Right?!? Have a look at [https://replit.com/@mohannadhussain/fhir-example](https://replit.com/@mohannadhussain/fhir-example)


## Resources
* [FHIR Home Page](https://www.hl7.org/fhir/index.html)
* [FHIR HAPI JPAServer Starter GitHub](https://github.com/hapifhir/hapi-fhir-jpaserver-starter)
* [Searching using FHIR](https://www.hl7.org/fhir/search.html)
* [Patient Resource](https://www.hl7.org/fhir/patient.html)


* [Python Package for FHIR resources](https://pypi.org/project/fhir.resources/)
* [Python Package - a FHIR Client](https://github.com/smart-on-fhir/client-py)

* [Python HL7 Package - GitHub](https://github.com/crs4/hl7apy)

## YouTube Video Channels for FHIR

* [Gino Canessa FHIR Tutorials](https://www.youtube.com/@GinoCanessa)
* [Sidharth Ramesh - MedBlocks FHIR Tutorials](https://www.youtube.com/@medblocks)

## FHIR Forums / User Groups

* [FHIR Chat - You can also use Zulip](https://chat.fhir.org/)
* [Zulip, client and server - Organized chat for distributed teams](https://zulip.com/)









