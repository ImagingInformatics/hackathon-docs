# Other noteworthy APIs, Standards and Utilities
**Note** If you are participaing in the SIIM Hackathon, you could get bonus points if your project incorporates emerging standards such as there below!

* [IHE AI Results (AIR)](https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_AIR_Rev1-0_PC_2020-03-10.pdf)

* [AI Workflow for Imaging (AIW-I)](https://wiki.ihe.net/index.php/Imaged-_Based_AI_Workflow_-_Brief_Proposal) - Hint: Use the [AI Orchestrator](../whats-new/2021.md).

* [IHE Whitepaper - AI Interoperability in Imaging](https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_White_Paper_AI_Interoperability_in_Imaging_Rev1-0_PC_2021-03-12.pdf)

* [FHIRcast](http://fhircast.org/) - Check out their [reference implementation](https://github.com/fhircast/sandbox) plus the [NodeJS port](https://github.com/fhircast/sandbox.js).

* Scan your code using SonarQube and include summaries of your findings (and things you learnt) in your showcase presentation (high-level overview, no need for detailed information or code samples).

* Even more bonus points if you are able to open-source your project code :)

## Can't get enough of this API goodness?
Here are some additional APIs and utilities that could help you create the ultimate mashup:

### [Open Health Imaging Foundation (OHIF)](http://ohif.org/)
The Open Health Imaging Foundation is developing an open source framework for constructing web-based medical imaging applications. The application framework is built using modern HTML/CSS/JavaScript and uses [Cornerstone](https://cornerstonejs.org/) at its core to display and manipulate medical images. It is built with Meteor, a Node.js-based full-stack JavaScript platform.

PS: Check out their awesome web-based DICOM viewer.

### [Static WADO-RS Generator](https://github.com/OHIF/static-wado) 
Allows you to simulate a DICOMweb server using static content, i.e. you would only need a simple HTTP server instead of a PACS system.

There are two versions: [Java](https://github.com/OHIF/static-wado-java) and [Javascript](https://github.com/OHIF/static-wado-js)

### [Synthea Synthetic Patient Generation](https://synthetichealth.github.io/synthea/)
Synthea is an open-source, synthetic patient generator that models the medical history of synthetic patients. Our mission is to provide high-quality, synthetic, realistic but not real, patient data and associated health records covering every aspect of healthcare. The resulting data is free from cost, privacy, and security restrictions, enabling research with Health IT data that is otherwise legally or practically unavailable.

### [Vonk Loader](https://simplifier.net/downloads/vonkloader) 
Vonk Loader is a command line tool to bulk load resources into a FHIR server. Vonk Loader works on Windows, Linux and macOS.

### [FHIR Resource Editor (FRED)](http://docs.smarthealthit.org/fred/)
Allows construction of FHIR object using a convenient user interface.

### [LOINC FHIR Terminology Server](https://loinc.org/fhir/)
You can LOINC content programmatically. Their server uses the terminology services defined by HL7's FHIR standard.

### [Radiology Gamuts Ontology API](http://www.gamuts.net/dev/)
The Gamuts.net site provides a REST API to aid developers in using Radiology Gamuts Ontology information.

### [RadReport API](http://www.radreport.org/dev/)
The Radreport.org site provides an API to aid developers in accessing structured report templates. The API provides a REST interface, which responds with JSON.

###  [RSNA RadLex Playbook](http://playbook.radlex.org/playbook/SearchRadlexAction)
RadLex Playbook is a project of the Radiological Society of North America (RSNA), and constitutes a portion of the [RadLex ontology](http://radlex.org/). Playbook aims to provide a standard system for naming radiology procedures, based on the elements which define an imaging exam such as modality and body part. By providing standard names and codes for radiologic studies, Playbook is intended to facilitate a variety of operational and quality improvement efforts, including workflow optimization, chargemaster management, radiation dose tracking, enterprise integration and image exchange.

The RadLEx Playbook User Guide can be found here in PDF format: 
http://playbook.radlex.org/playbook-user-guide.pdf?newfile=1
