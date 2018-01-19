# Blockchain 
### Christian Sindt, Kasper Pontoppidan & Kasper Olesen 


## The application 

Our system consists of 1 python file, located in the /blockchain folder:
``` python
block.py

```
To start the peer-to-peer network, we use 1 DockerFile and 1 docker-compose.yml file.
The nodes in the peer-to-peer network, will run by default on localhost:5000

### Endpoints

GET - nodes/mine/hash (Mining version 1)

GET - nodes/mine/modulo (Mining version 2)

GET - nodes/chain

GET - nodes/resolve

Transaction structure:

```
{
	"amount": someNumber,
	
	"sender": "someValue",

	"recipient": "someOtherValue"
}
```

## How to run

Our system depends on Docker and Docker-compose. 
To install, run:
``` $$bash
bash install.sh

```

To start our blockchain application run:
``` $$bash
bash run.sh

```
This will run the docker-compose file(in the root of the repository), and start up 4 containers, which uses the DockerFile to download the python:3 image, installing all the dependencies and requirements and finally running the block.py service.

**Start-up:**

![run](https://user-images.githubusercontent.com/11289686/35142540-ecd920ac-fcfe-11e7-991d-6716f66e5555.PNG)


### Mining example:
Request on node 1 (:10006) 
http://localhost:10006/mine/hash

In our first mining version, we have created a proof of work algorithm that should: "Find a number (proof in the example) that when hashed with the previous block’s solution, resulting in a hash with 4 leading 0s". The miners are then rewarded for their solution by receiving 1 coin by the network, this is stored in a transaction.

![mine](https://user-images.githubusercontent.com/11289686/35143457-e80643ea-fd01-11e7-8206-67eb1106139d.PNG)


For every successful mining, we add another block to the nodes copy of the blockchain, so if we do this 3 times we get an chain of 4 blocks (because all nodes, already got the first genesis block) , see the chain example:

http://localhost:10006/chain

![chain-mined](https://user-images.githubusercontent.com/11289686/35144042-a7cb505c-fd03-11e7-8d43-792820cea6ac.PNG)


### Consensus example:
As mentioned our node 1, now has a blockchain with the length of 4, but the other nodes in our network, still got a different copy of the blockchain.

Request: http://localhost:10007/chain

![chain](https://user-images.githubusercontent.com/11289686/35144453-dcdc4390-fd04-11e7-8c9f-4c8d2e249620.PNG)

We need to ensure that they all reflect the same chain, for that we have implementet a Consensus Algorithm, so that we can have more than one node in our network. The rule in our Consensus algorithm is, that the longest valid chain in the network is authoritative.

So when we go to:
Request: http://localhost:10007/nodes/resolve

Node 2, ask's all the other nodes in the network, for a copy of their blockchain, and run them through the consensus algorithm.

**Result:**

![resolved](https://user-images.githubusercontent.com/11289686/35144650-67ef89b0-fd05-11e7-8866-800aefcb547f.PNG)


### Mining version 2 example:
On the same way as the first mining version we will have to increment a number. When that number is divisible by 9, and the proof number of the last block, a new block is mined, and a new coin is rewarded in a transaction: 

**Mining on node 2**

Request: http://localhost:10007/mine/modulo

![mine2](https://user-images.githubusercontent.com/11289686/35145159-22de5c28-fd07-11e7-837a-d5967dc9e954.PNG)


To make sure, node 2 still got the longest valid chain we make another resovle request:

Request: http://localhost:10007/nodes/resolve

![resolved2](https://user-images.githubusercontent.com/11289686/35145392-f0592610-fd07-11e7-9719-6931c780dbc2.PNG)


As we can see, node 2 still got the longest valid chain, including our new mined block.

## Sources

(1) https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

(2) https://github.com/davecan/easychain

(3) https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d

(4) https://www.oreilly.com/learning/what-is-docker-networking

(5) https://docs.docker.com/compose/compose-file/
