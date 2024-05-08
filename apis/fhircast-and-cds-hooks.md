# FHIR-related Technologies
Although the FHIR standard solves many problems, some were out of scope for the core standard. Therefore, there are technologies adjacent to FHIR-itself to help with certain use cases.


## FHIRcast
When clinicians work on a computer, they typically find themselves working in multiple applications on the same patient record(s). Take Radiologists for example, they would typically have three applications open:
1. Electronic Medical Record (EMR) to reference the patient's record. E.g. patient demographics, medical history and medications.
2. Picture Archiving and Communication System (PACS) client to review/read the actual Radiology images.
3. Reporting application, sometimes called voice recognition (VR) because they typically dictate reports via microphone rather than type them in on a keyboard.
All these applications ALREADY talk to each other on the backend, i.e. server to server. However, they also need to talk to each other directly on the computer itself, i.e. the front-end. Sometimes this is called a desktop integration, or context synhronization.

A previous standard named CCOW largely failed to standardadize these desktop integrations. So FHIRcast was conceived as a fresh attempt to inject interoperability into these integrations, and so far it is gaining plenty of momentum and real-world implementations.

Find out more via [FHIRcast's homepage](https://fhircast.org/).


## SMART on FHIR
A common workflow is the need for an end user, e.g. clinician, to launch an application right from within the EMR in context. The launched application would provide additional functionality, e.g. an application to help manage diabetic patients. The industry had figured out ways to launch such apps in context (i.e. launch it with parameters so it displays the current patients' record). However, not only were these implementations non-standardized, they also left more to be desired (which, you guessed it, SMART on FHIR solves for):
1. Single-Sign On (SSO) so the end user does not have to re-enter their password.
2. More than just contextual launch, but rather locking the launched application scope to a specific scope. For example, the launched app should only be able to diplay information about patient X during this given session.

Here's a [quick primer on SMART on FHIR](https://smarthealthit.org/smart-on-fhir-api/), as well as some [documentation](https://docs.smarthealthit.org/).


## CDS Hooks
Although EMRs have grown to be very comprehensive, there are still use cases that need specialized software. As you've seen above, SMART on FHIR solves for launching another application from within the EMR. But what about a less disruptive workflow the seamlessly blends in? Enter CDS Hooks. 

CDS Hooks allow the EMR to send notifications to other software without launching them outright. These notifications are fired off based on triggers (example coming soon). The other software (sometimes called remote service) can then request the EMR to show a "card" (i.e. pop-up notifications), which could show one of three things:
1. Simple text-based card
2. Card combining text along with a suggestion
3. Card combining text along with a link to launch a SMART on FHIR app.

Here's a practical example of how this would be useful in the real world. Say the clinician is about to prescribe medication to their patient. The action of creating a prescribtion triggers a notification to a another software which knows to check the patient's record for existing medications and potential clashes/allergies/toxicity. That software can then decide to have the EMR show cards based on the outcome:
1. Simple card telling the clinician the new medicaiton is OK to prescribe, which is reassuring.
2. Card suggesting another medication. It could be due to insruance coverage differences, or perhaps the patient has allergies to certain drugs.
3. Say the other software needed to present the clinician with additional information (extra paperwork required to prescribe this drug to override a detected clash), it could present a card with a link to launch the software's user interface.

Read more about [CDS Hooks via their homepage](https://cds-hooks.org/).

