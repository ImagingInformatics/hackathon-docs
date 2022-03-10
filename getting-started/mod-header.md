# ModHeader for in-browser exploration of Hackathon APIs

All the APIs hosted on the Hackathon server require an API key to be sent via an HTTP header, which is easy to do using a tool like Postman or curl, but not very straightforward right from within the browser.

You can obtain a plugin/extension to enable most modern browsers to do this. For example, [ModHeader for Chrome](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en) can enable this for Chrome users.

## Configuration
Said browser plugins allow you to send specific headers to specific sites. Using the example of ModHeader, you can configured it like so:
* **Request Headers** `apikey: [your-api-key]`
    Replace [your-api-key] with your private API key.
* **Filters** To ensure your API is not to any other Internet website, add the following entries:
`https://hackathon.siim.org/.*` and `http://hackathon.siim.org/.*`

You now should be able to navigate to URLs like https://hackathon.siim.org/ or https://hackathon.siim.org/vna and use them in your browser.
