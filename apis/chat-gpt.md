# Generative Pretrained Transformer (GPT, aka ChatGPT)

## GPT? ChatGPT? What's The Difference?
GPT, or Generative Pre-trained Transformer, is a language model architecture developed by OpenAI. It is trained on a large corpus of text data to generate coherent and contextually relevant responses to given prompts. When you use the API to query the server, you are interacting with a GPT model.  GPT has may variants, each specialized to do something slightly different, including Chat Completion, which brings us to... ChatGPT generally refers to a non-API consumer interface using GPT specifically designed for conversational interactions. It focuses on generating coherent responses in a conversational context. ChatGPT is fine-tuned using reinforcement learning from human feedback to improve the quality of its responses. This fine-tuning process helps ChatGPT produce more engaging and contextually appropriate replies during conversational exchanges.

## Introduction
Interested in trying out OpenAI's GPT? Thanks to our friends at [MD.ai](https://md.ai/), we have a proxy in place that allows you to perform API calls to both GPT versions 3.5 and 4.0. The proxy utilizes md.ai credits with every account starting with 1000 free credits. Go to [siim.md.ai](https://siim.md.ai/) and sign up for a free account to secure your credits.

This is a quick starting guide. If you want a more detailed version, please see [Using GPT for Medical Imaging and Data Analysis in the SIIM Hackathon](https://colab.research.google.com/drive/1V_UthmhzQMR4GCQRuNUQGgHVp93iGCCw?usp=sharing), thanks to [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/).

You can use OpenAI's GPT to generate code samples, ask it Imaging Informatics questions, etc. Please share on Slack what you're using GPT for and how useful you found it to be.

### GPT 3.5 vs 4
Below is a quick comparison to help you plan accordingly:

| Generation  | Speed                  | Intelligence & Accuracy | Cost/API Call | # of calls for 1000 credits |
|-------------|------------------------|-----------------------|---------------|----------------------------------------------|
| GPT 3.5 | Fast (tens of seconds) | Good                  | 1             | 1000                                         |
| GPT 4   | Slow (several minutes) | Great                 | 10            | 100                                           |

## How to use the Chat GPT Proxy
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

## Getting an API Key
Go to [siim.md.ai](https://siim.md.ai/) and sign up for a free account. Once logged in, click your Initials/Avatar in the top right corner and select `User Settings`. In the next screen, select `Access Tokens` and proceed to `Generate New Token`. Once you have a token, you can use it in your code as your MD.ai API key.

## Sample Notebooks
* A more detailed version of this guide, [Using GPT for Medical Imaging and Data Analysis in the SIIM Hackathon](https://colab.research.google.com/gist/georgezero/2e52ca00dcfade8ec4dad553657074a7/using-gpt-for-medical-imaging-and-data-analysis-in-the-siim-hackathon-rev-20230606.ipynb), thanks to [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/)
* Example asking GPT to generate a Jupyter Notebook doing FHIR and DICOMweb API Calls. One [Using GPT 4](https://colab.research.google.com/gist/georgezero/5e47d843357fa57286ef8c25e13c25b2/mdai-gpt-4-api-demo.ipynb) and another [Using GPT 3.5](https://colab.research.google.com/gist/georgezero/ab60da51114fe57089b29feb676c35f7/mdai-gpt-4-api-demo.ipynb) or [Compare both side-by-side](https://colab.research.google.com/gist/georgezero/c5582934e980eeabcf38ad6d648cc4d9/mdai-gpt-4-api-demo.ipynb), thanks to [Dr. George Shih](https://www.linkedin.com/in/georgenyc/).

## Keep in mind...

Please note that OpenAI's GPT generated code only serves a starting point and may not work as-is against the Hackathon server for a variety of reasons. Some basic troubleshooting and minor tweaks might be necessary. Don't be afraid to ask for help if you get stuck!


## Aknowledgements
This guide, and API access would not be possible with the help of some awesome people!!

1. [MD.ai](https://md.ai) and especially [Dr. George Shih](https://www.linkedin.com/in/georgenyc/) generously sharing OpenAI GPT API access.
2. [Dr. Howard Chen](https://www.linkedin.com/in/howard-po-hao-chen-a04b082a/) taking time to diligently document and test the steps involved in this process.
3. [Dr. Stephanie Hou](https://www.linkedin.com/in/stephanie-hou-5269201a9/) for reviewing, editing, commenting, making suggestions, etc.




