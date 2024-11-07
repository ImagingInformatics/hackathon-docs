# Contributing
We are glad that you are thinking about contributing. See below for options...

## This Documentation
Do you see a spelling error? Or maybe you have some cool information to add? We'd love to incorporate your changes.

Everything you see in these docs is authored using [Markdown](https://en.wikipedia.org/wiki/Markdown) in Github. Simply fork this project [https://github.com/ImagingInformatics/hackathon-docs](https://github.com/ImagingInformatics/hackathon-docs), make your changes then submit a pull request.

To work on the documentation you do need to have Python installed and you will need to install some Python packages:

```
pip3 install mkdocs
pip3 install mkdocs-same-dir
```

After that, simply execute the following.

```
mkdocs serve
```

and visit:  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

There is more documentation about MkDocs here:  [MkDocs User Guide](https://www.mkdocs.org/user-guide/)

## SIIM Hackathon Dataset
We are always in search of volunteers to help enrich our dataset. Below are some ideas for things people can contribute, but we are definitely open to other ideas as well.

* Incorporate non-Radiology samples (e.g. Dermatology or Pathology) into one of the patient vignette
* Expand the number of featured FHIR resources, e.g. add some `Immunization` or `Medication` resources.
* Enrich existing resources by adding more information, e.g. adding a preliminary report, or an addendum.
* Update our resources for future-proofing against upcoming versions of FHIR
* Incorporate AI-result samples, e.g. DICOM SR TID 1500 and/or FHIR `Observation`

You can simply fork the project from GitHub here [https://github.com/ImagingInformatics/hackathon-dataset](https://github.com/ImagingInformatics/hackathon-dataset), make your changes then submit a pull request.

### How to add new patient's data on the Dataset from existing dicom files?

#### 1. Fork the two repositories for the [dataset](https://github.com/ImagingInformatics/hackathon-dataset.git) and the [images](https://github.com/ImagingInformatics/hackathon-images.git) and clone your forks locally.
#### 2. Update the dicom fields of the images you want to add in the dataset
* Use [pydicom](https://pydicom.github.io/) to update the dicom fields of the images you want to contribute. (ps: other dicom libraries can be used as well, like (dcm4che)[https://www.dcm4che.org/])
* The non-exhaustive list of fields to update from existing dicom files are:  

| Field            | Value                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| PatientID        | PatientID of the patient you want to contribute. e.g. breastdx-01-0003                                          |
| PatientName      | PatientName of the patient you want to contribute. Look at the dataset repository for existing names e.g. Sally |
| AccessionNumber  | Unique number identifying the study in the system (HIS/RIS). e.g. a330740045455447                              |
| PatientBirthDate | Birth date of the patient. Ideally, patient age should be between 40-60 years old. e.g. 19500825                |
| StudyDate        | Date of the study if not provided. e.g. 20190101                                                                |
| PatientAge       | Age of the patient. Should be the difference between StudyDate and PatientBirthDate. e.g. 049Y                  |

* Save the modified dicom files in the following directory structure:  
````bash
/{patient_name} SIIM/

Example with patient Sally:

/Sally SIIM/
````
#### 3. Create the FHIR resources of the patient you want to contribute
* Start by creating a patient resource if it does not exist in the dataset repository. Use existing patient resource as template and
update the resource id, text, name, gender, and birth date fields according the patient data.
* Create an imaging study resource for the patient from the dicom files. Use [dicom2fhir](https://github.com/LinuxForHealth/dicom-fhir-converter.git) script
as a starting point for the imaging resource.
* Modify the imaging study resource to fit the SIIM Hackathon dataset format. Here are a not exhaustive list of fields to update manually:

| Field                         | Value                                             |
|-------------------------------|---------------------------------------------------|
| identifier.assigner.reference | Organisation/siim                                 |
| subject.reference             | Patient/siim{patient_name} e.g. Patient/siimsally |
| endpoint                      | Endpoint/siim-dicomweb                            |

* Move the fhir files imaging study and patient into the following directory structure  
````bash
/siim_{patient_name}_{patient_id}/ImagingStudy/imaging_study.{series_id}.json
/siim_{patient_name}_{patient_id}/Patient/patient.{patient_id}.json

Example with patient Sally and with patient id breastdx-01-0003:

/siim_sally_breastdx-01-0003/ImagingStudy/imaging_study.1.2.276.0.7230010.3.1.4.8323329.1000.1517875209.100000.json
/siim_sally_breastdx-01-0003/Patient/patient.breastdx-01-0003.json
````

#### 4. Create a pull request for the dataset and images repositories
