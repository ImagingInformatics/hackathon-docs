# 5-Minute Ethereum Starting Guide

## Basic Concepts
* Ethereum is one implementation of Blockchain, others exist, too, like BitCoin.
* Although most Blockchain implementations focus on monetary transactions, they support other concepts like [NFT](https://en.wikipedia.org/wiki/Non-fungible_token).
* We believe Blockchain has a role to play in improving healthcare record storage due to its write-once, read-many time nature.
* Some sample healthcare application ideas: 
  * Initiation and verification of physician credentialing
  * Vaccine certification and verification

## Prerequesities
1. [SIIM Hackathon API key](../getting-started/hackathon-server.md)
2. [Postman](https://www.postman.com/)


## 1. Set up
1. Launch Postman
2. Create a new request
3. Click the `GET` dropdown next to the URL, and change it to `POST`
4. Set the request URL to `http://hackathon.siim.org/ethereum/` **NOTE http NOT https**
5. Click the `Headers` tab (under the URL) and set the following headers:
    A. `apikey` with a value of your SIIM Hackathon API Key
    B. `Content-Type` with a value of `application/json`
6. Click the `Body` tab (under the URL) and select `Raw` then change the `Text` dropdown that appeared on the right to `JSON`
7. The empty white space below is where you will copy/paste the API calls seen below


## 2. Check the list of nodes/peers
This is useful to know the size of the network, i.e. the number of entities actively connected to it (Hint: our network is private so it should be one).

Copy/paste the following API call in the Request Body, then hit the blue `Send` button. You should see results in the `Response` pane.
```
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "admin_peers",
    "params": []
}
```

## 3. Get the latest block number
This tells us how long the "chain" is in this network, which provides an idea of how many transactions have taken place.

Just like step 2, but with this API call instead:
```
{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "eth_blockNumber",
    "params": []
}
```

## 4. Get the list of accounts
Just like you can have multiple accounts with a bank, the same concept applies here, too. This call lists all known accounts

Just like step 2, but with this API call instead:
```
{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "eth_accounts",
    "params": []
}
```

## 5. Get the balance of an account
Just like checking the balance on your real-life bank account, except in Ethereum the balance is in [hexadecimal](https://www.google.com/search?q=hexadecimal+to+decimal+converter) number and in [wei unit](https://ethdocs.org/en/latest/ether.html).

Just like step 2, but with this API call instead:
```
{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "eth_getBalance",
    "params": [
        "0x0000000000000000000000000000000000000001",
        "latest"
    ]
}
```
**NOTE** The call above checks the balance of account number `0x0000000000000000000000000000000000000001` specifically. If you want to check another account, replace that value with another account number seen in the response from the previous step.


## Resources
* [Running a Private Ethereum Blockchain using Docker](https://medium.com/scb-digital/running-a-private-ethereum-blockchain-using-docker-589c8e6a4fe8)
* [Ethereum Homepage](https://ethereum.org/en/)