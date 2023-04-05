# 5-Minute Ethereum Starting Guide

## Basic Concepts
* Ethereum is one implementation of Blockchain, others exist, too, like BitCoin.
* Although most Blockchain implementations focus on monetary transactions, they support other concepts like [NFT](https://en.wikipedia.org/wiki/Non-fungible_token).
* We believe Blockchain has a role to play in improving healthcare record storage due to its write-once, read-many time nature.
* Some sample healthcare application ideas: 
  * Initiation and verification of physician credentialing
  * Vaccine certification and verification

## Prerequisites
1. [Docker](https://www.docker.com/)
2. [Postman](https://www.postman.com/)

## 1. Ethereum Docker Set Up
### 1a. Required Files
Create a folder to keep all things related to Ethereum in one place. The under that folder create the following files with their contents:
#### .env
```
# The ID of Ethereum Network
NETWORK_ID=1214

# The password to create and access the primary account
ACCOUNT_PASSWORD=supersecretpassword
```
#### Dockerfile
```
FROM ethereum/client-go:v1.10.1

ARG ACCOUNT_PASSWORD

COPY genesis.json /tmp

RUN geth init /tmp/genesis.json \
    && rm -f ~/.ethereum/geth/nodekey \
    && echo ${ACCOUNT_PASSWORD} > /tmp/password \
    && geth account new --password /tmp/password \
    && rm -f /tmp/password

ENTRYPOINT ["geth"]
```
#### docker-compose.yml
```
version: '3.7'

services:
  geth-bootnode:
    hostname: geth-bootnode
    env_file:
      - .env
    image: geth-client
    build:
      context: .
      args:
        - ACCOUNT_PASSWORD=${ACCOUNT_PASSWORD}
    command:
      --nodekeyhex="b0ac22adcad37213c7c565810a50f1772291e7b0ce53fb73e7ec2a3c75bc13b5"
      --nodiscover
      --ipcdisable
      --networkid=${NETWORK_ID}
      #--netrestrict="172.16.254.0/28"
    networks:
      priv-eth-net:

  geth-rpc-endpoint:
    hostname: geth-rpc-endpoint
    env_file:
      - .env
    image: geth-client
    depends_on:
      - geth-bootnode    
    command:
      --bootnodes="enode://af22c29c316ad069cf48a09a4ad5cf04a251b411e45098888d114c6dd7f489a13786620d5953738762afa13711d4ffb3b19aa5de772d8af72f851f7e9c5b164a@geth-bootnode:30303"
      --allow-insecure-unlock
      --http
      --http.addr="0.0.0.0"
      --http.api="eth,web3,net,admin,personal"
      --http.corsdomain="*"
      --networkid=${NETWORK_ID}
      --rpcvhosts=*
      #--netrestrict="172.16.254.0/28"
    ports:
      - "8545:8545"
    networks:
      priv-eth-net:

  geth-miner:
    hostname: geth-miner
    env_file:
      - .env
    image: geth-client
    depends_on:
      - geth-bootnode
    command:
      --bootnodes="enode://af22c29c316ad069cf48a09a4ad5cf04a251b411e45098888d114c6dd7f489a13786620d5953738762afa13711d4ffb3b19aa5de772d8af72f851f7e9c5b164a@geth-bootnode:30303"
      --mine
      --miner.threads=1
      --networkid=${NETWORK_ID}
      #--netrestrict="172.16.254.0/28"
    networks:
      priv-eth-net:

networks:
  priv-eth-net:
    driver: bridge
    ipam:
      config:
      - subnet: 172.16.254.0/28
```
#### genesis.json
```
{
  "config": {
    "chainId": 1214,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "ethash": {}
  },
  "difficulty": "1",
  "gasLimit": "12000000",
  "alloc": {
      "0x0000000000000000000000000000000000000001": {
      "balance": "111111111"
    },
      "0x0000000000000000000000000000000000000002": {
      "balance": "222222222"
    }
  }
}

```
### 1b. Running it
Under your folder, you can run to start it:
```
docker-compose up -d
```
To stop it:
```
docker-compose down -v
```

If you find it using too much CPU, you can restrict its CPU usage like so:
```
docker update --cpu-shares=100 ethereum_geth-miner_1
docker update --cpu-shares=100 ethereum_geth-rpc-endpoint_1
docker update --cpu-shares=100 ethereum_geth-bootnode_1
```


## 2. Postman Set Up
1. Launch Postman
2. Create a new request
3. Click the `GET` dropdown next to the URL, and change it to `POST`
4. Set the request URL to `http://localhost:8545/` **NOTE http NOT https**
5. Click the `Headers` tab (under the URL) and set the header `Content-Type` with a value of `application/json`
6. Click the `Body` tab (under the URL) and select `Raw` then change the `Text` dropdown that appeared on the right to `JSON`
7. The empty white space below is where you will copy/paste the API calls seen below


## 3. Check the list of nodes/peers
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

## 4. Get the latest block number
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

## 5. Get the list of accounts
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

## 6. Get the balance of an account
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
* *Wallet apps* can make it easier to work with Blockchain networks (Ethereum or otherwise). Below are some examples to explore:
  * [MetaMask](https://metamask.io/)
  * [Trust Wallet](https://trustwallet.com/)
  * [Ledger Hardware Wallet](https://www.ledger.com/)
  * [Math Wallet](https://mathwallet.org)
  * [Brave Browser](https://brave.com/) has a basic built-in wallet
