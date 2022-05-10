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


## Resources
* [Unofficial FHIR Starter Guide](http://www.learnfhir.com)
* [FHIR Home Page](https://www.hl7.org/fhir/index.html)
* [Searching using FHIR](https://www.hl7.org/fhir/search.html)
* [Patient Resource](https://www.hl7.org/fhir/patient.html)
