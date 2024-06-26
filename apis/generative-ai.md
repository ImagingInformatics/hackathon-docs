# Generative AI

On this page, we'll list a number of Generative AI (e.g. Large Language Model) that you can access. They are: GPT (aka ChatGPT), NVIDIA's build page and more will come soon.



## NVIDIA's Build Page

NVIDIA hosts a number of open-source Generative AI models at [build.nvidia.com](https://build.nvidia.com/). The models range from Large Language Models (e.g. llama) to visual models (generate images based on textual prompts) and many other categories. Additionally, the website allows you to try out the different models without having to login. It makes for a nice way to get a feel for what each model is capable of, but also to try these models before you invest time/money into hosting your own copy of them. 



## Generative Pretrained Transformer (GPT, aka ChatGPT)

### GPT? ChatGPT? What's The Difference?
GPT, or Generative Pre-trained Transformer, is a language model architecture developed by OpenAI. It is trained on a large corpus of text data to generate coherent and contextually relevant responses to given prompts. When you use the API to query the server, you are interacting with a GPT model.  GPT has many variants, each specialized to do something slightly different, including Chat Completion, which brings us to... ChatGPT generally refers to a non-API consumer interface using GPT specifically designed for conversational interactions. It focuses on generating coherent responses in a conversational context. ChatGPT is fine-tuned using reinforcement learning from human feedback to improve the quality of its responses. This fine-tuning process helps ChatGPT produce more engaging and contextually appropriate replies during conversational exchanges.

### Introduction
Interested in trying out OpenAI's GPT? Thanks to our friends at [MD.ai](https://md.ai/), we have a proxy in place that allows you to perform API calls to both GPT versions 3.5 and 4.0. The proxy utilizes md.ai credits with every account starting with 1000 free credits. Go to [siim.md.ai](https://siim.md.ai/) and sign up for a free account to secure your credits.

This is a quick starting guide. If you want a more detailed version, please see [Using GPT for Medical Imaging and Data Analysis in the SIIM Hackathon](https://colab.research.google.com/drive/1V_UthmhzQMR4GCQRuNUQGgHVp93iGCCw?usp=sharing), thanks to [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/).

You can use OpenAI's GPT to generate code samples, ask it Imaging Informatics questions, etc. Please share on Slack what you're using GPT for and how useful you found it to be.

#### GPT 3.5 vs 4
Below is a quick comparison to help you plan accordingly:

| Generation  | Speed                  | Intelligence & Accuracy | Cost/API Call | # of calls for 1000 credits |
|-------------|------------------------|-----------------------|---------------|----------------------------------------------|
| GPT 3.5 | Fast (tens of seconds) | Good                  | 1             | 1000                                         |
| GPT 4   | Slow (several minutes) | Great                 | 10            | 100                                           |

### How to use the Chat GPT Proxy
Make an HTTP POST to `https://siim.md.ai/api/openai/chat/completions`
With the following HTTP headers:

* `Content-Type`: `application/json`
* `x-access-token`: *YOUR_MDAI_API_KEY*

And the following JSON Payload:
```
{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "your question or prompt goes here"}]
  }
```
You may substitute `gpt-4` with `gpt-3.5-turbo` to address different GPT versions. **Note:** See the notebook examples below for additional optional parameters you can specify to tweak model performance and output.

Your results will be served back in JSON format.

See the Sample Notebooks section below for working code examples.

### Getting an API Key
1. Go to [siim.md.ai/chat](https://siim.md.ai/chat) and sign up for a free account. 
2. Once logged in, click the settings (gear) icon in the top right corner and select `Access Tokens`. 
3. There, click `+ Generate` to generate a new token, give it a name (e.g. `my token`) then click `Confirm`. 
4. Once that's done, copy the token displayed and save it somewhere handy. 
5. Use your token in your code and/or API calls as your MD.ai API key.

### Sample Notebooks
* A more detailed version of this guide, [Using GPT for Medical Imaging and Data Analysis in the SIIM Hackathon](https://colab.research.google.com/gist/georgezero/2e52ca00dcfade8ec4dad553657074a7/using-gpt-for-medical-imaging-and-data-analysis-in-the-siim-hackathon-rev-20230606.ipynb), thanks to [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/)
* Example asking GPT to generate a Jupyter Notebook doing FHIR and DICOMweb API Calls. One [Using GPT 4](https://colab.research.google.com/gist/georgezero/98069d9133b2d45b90d03dd53bc488dc/mdai-gpt-4-api-siim-hackathon-2023-example-rev-20230606.ipynb) and another [Using GPT 3.5 side-by-side with GPT 4](https://colab.research.google.com/gist/georgezero/f9d87413469663b37a5801968d027596/mdai-gpt4-and-gpt35-api-siim-hackathon-2023-example-ipynb-rev-20230606.ipynb), thanks to [Dr. George Shih](https://www.linkedin.com/in/georgenyc/).

### Keep in mind...

Please note that OpenAI's GPT generated code only serves a starting point and may not work as-is against the Hackathon server for a variety of reasons. Some basic troubleshooting and minor tweaks might be necessary. Don't be afraid to ask for help if you get stuck!



## Aknowledgements
This guide, and API access would not be possible with the help of some awesome people!!

1. [MD.ai](https://md.ai) and especially [Dr. George Shih](https://www.linkedin.com/in/georgenyc/) generously sharing OpenAI GPT API access.
2. [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/) taking time to diligently document and test the steps involved in this process.
3. [Dr. Stephanie Hou](https://www.linkedin.com/in/stephanie-hou-5269201a9/) for reviewing, editing, commenting, making suggestions, etc.




