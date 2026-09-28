# Generative AI

On this page, we'll list a number of Generative AI (e.g. Large Language Model) resources you can access. Currently that's NVIDIA's build page, below. The GPT proxy that previous hackathons offered through MD.ai is no longer available; see the note in that section.



## NVIDIA's Build Page

NVIDIA hosts a number of open-source Generative AI models at [build.nvidia.com](https://build.nvidia.com/). The models range from Large Language Models (e.g. llama) to visual models (generate images based on textual prompts) and many other categories. Additionally, the website allows you to try out the different models without having to login. It makes for a nice way to get a feel for what each model is capable of, but also to try these models before you invest time/money into hosting your own copy of them. 



## Generative Pretrained Transformer (GPT, aka ChatGPT)

### GPT? ChatGPT? What's The Difference?
GPT, or Generative Pre-trained Transformer, is a language model architecture developed by OpenAI. It is trained on a large corpus of text data to generate coherent and contextually relevant responses to given prompts. When you use the API to query the server, you are interacting with a GPT model.  GPT has many variants, each specialized to do something slightly different, including Chat Completion, which brings us to... ChatGPT generally refers to a non-API consumer interface using GPT specifically designed for conversational interactions. It focuses on generating coherent responses in a conversational context. ChatGPT is fine-tuned using reinforcement learning from human feedback to improve the quality of its responses. This fine-tuning process helps ChatGPT produce more engaging and contextually appropriate replies during conversational exchanges.

> **The SIIM GPT proxy is no longer available.** Previous hackathons offered free GPT access
> through a proxy hosted by [MD.ai](https://md.ai/) at `siim.md.ai`. That address no longer serves
> the proxy, so the sign-up, API key and endpoint instructions that used to be here have been
> removed. If you want to use GPT at the hackathon, you will need your own
> [OpenAI API key](https://platform.openai.com/). The models on
> [NVIDIA's build page](#nvidias-build-page) above can also be tried without logging in.

You can use GPT to generate code samples, ask it Imaging Informatics questions, etc. Please share on Slack what you're using it for and how useful you found it to be.

### Sample Notebooks
These notebooks were written for the MD.ai proxy. They are still worth reading as worked examples of
using GPT against the Hackathon APIs, but they call the retired `siim.md.ai` endpoint, so they will
need adapting to your own API key before they run.

* [Using GPT for Medical Imaging and Data Analysis in the SIIM Hackathon](https://colab.research.google.com/gist/georgezero/2e52ca00dcfade8ec4dad553657074a7/using-gpt-for-medical-imaging-and-data-analysis-in-the-siim-hackathon-rev-20230606.ipynb), thanks to [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/)
* Example asking GPT to generate a Jupyter Notebook doing FHIR and DICOMweb API Calls. One [Using GPT 4](https://colab.research.google.com/gist/georgezero/98069d9133b2d45b90d03dd53bc488dc/mdai-gpt-4-api-siim-hackathon-2023-example-rev-20230606.ipynb) and another [Using GPT 3.5 side-by-side with GPT 4](https://colab.research.google.com/gist/georgezero/f9d87413469663b37a5801968d027596/mdai-gpt4-and-gpt35-api-siim-hackathon-2023-example-ipynb-rev-20230606.ipynb), thanks to [Dr. George Shih](https://www.linkedin.com/in/georgenyc/).

### Keep in mind...

Please note that OpenAI's GPT generated code only serves a starting point and may not work as-is against the Hackathon server for a variety of reasons. Some basic troubleshooting and minor tweaks might be necessary. Don't be afraid to ask for help if you get stuck!



## Acknowledgements
This guide, and the GPT access previous hackathons enjoyed, would not have been possible without some awesome people!!

1. [MD.ai](https://md.ai) and especially [Dr. George Shih](https://www.linkedin.com/in/georgenyc/) for generously sharing OpenAI GPT API access with past hackathons.
2. [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/) taking time to diligently document and test the steps involved in this process.
3. [Dr. Stephanie Hou](https://www.linkedin.com/in/stephanie-hou-5269201a9/) for reviewing, editing, commenting, making suggestions, etc.




