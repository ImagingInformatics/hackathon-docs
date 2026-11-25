# 2026 SIIM Hackathon
The 2026 SIIM Hackathon ran in **hybrid** format again. Everyone was welcome, and no coding experience was required. People could take part 100% virtually, with some optional in-person activities at [SIIM 26](https://annualmeeting.siim.org/) in Pittsburgh, PA (June 10-12). Keep an eye on the [SIIM Hackathon Page](https://siim.org/learning-events/events/hackathon/) for news about the next hackathon.


The SIIM Hackathon is open to all walks of life, whether you are clinical, technical or something else - we want YOU! In true SIIM spirit, the hackathon is focused on education and collaboration above all else. Come in groups or individually - we can pair you with others. The hackathon is not a full-time engagement, meaning, you can join us with any amount of free time you have.

The SIIM Hackathon features imaging informatics APIs like DICOMweb and FHIR among others, along with an open-source dataset showing how clinical and imaging data integrate. Go to [What's new in 2026](../whats-new/2026.md) to find out new and exciting things happening this year.

## How can I participate?

Go to the [Hackathon page on siim.org](https://siim.org/learning-events/events/hackathon/) and ensure you are registered for the hackathon via the green registration button on the right-hand side. We'll then get in touch with you to announce upcoming sessions of interest.

Additionally, don't forget to join the conversation on [Slack](https://join.slack.com/t/siimhackathon/shared_invite/zt-mkk0yn2e-KUqOLi6ETBUQmOffxmcQxA). 

For inspiration of ideas to implement, check this [list of hackathon project ideas](https://docs.google.com/spreadsheets/d/160Ph4t0BxKb1L-Mv_Bq7867yHEXonBxrslgUf-EixmY/edit?usp=sharing).

You can also take time to familiarize yourself with the [Hackathon Server](./hackathon-server.md) and its APIs. As well as [resources of interest](../apis/other-apis-and-standards.md).


## Questions? Problems?
Seek help by posting a message on Slack in `#general`. During the hackathon event, we have code heroes to help with technical matters in `#code-heroes`, and domain experts to help with clinical workflows and domain knowledge in `#domain-experts`.

If you need help outside the hackathon event or for any other urgent matters, please contact Thomas O'Sullivan at [Thomas.Liam.OSullivan@gmail.com](mailto:Thomas.Liam.OSullivan@gmail.com), or `@TomO` on the Hackathon Slack space. For a broken link or a mistake in these docs, you can also [open an issue on GitHub](https://github.com/ImagingInformatics/hackathon-docs/issues).

## Some things to keep in mind!
* SIIM's hackathon dataset provides **ten** cohesive patient stories that connect the FHIR and DICOMweb resources like a real-life patient would have. Their ids all start with `siim` (for example `siimandy`). Nine of them have the last name `SIIM`, so `Patient?family=SIIM` finds those nine. The tenth is Bibata Amadou (`Patient/siimbibata`).
* Our FHIR server comes in two versions of the standard: R5 (`https://hackathon.siim.org/fhir/`) and R4 (`https://hackathon.siim.org/fhir-r4/`).
* Both FHIR servers also have the same 40 synthetic patients made with [Synthea](https://synthetichealth.github.io/synthea/), each with about 10 years of history (encounters, conditions, labs, medications, procedures). That makes 50 baseline patients on each server, plus anything teams upload before the next daily reset. The Synthea patients have generated ids instead of `siim` ones and no images on the DICOMweb server. List the 50 baseline patients with `Patient?_count=50`. Some have thousands of resources, so `Patient/[id]/$everything` comes back in pages. Follow the `next` links.
* Our DICOMweb server may not support every feature described in the DICOMweb specifications. Check [Orthanc's DICOMweb status page](https://orthanc.uclouvain.be/hg/orthanc-dicomweb/file/tip/Status.txt) for more details.
