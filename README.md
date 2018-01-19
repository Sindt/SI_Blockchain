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
This will run the docker-compose file(in the root of the repository), and start up 4 containers, which uses the DockerFile to download the python:3 image, installing all the dependencies and requirements and finally running the block.py serivce.

**Start-up:**

![run](https://user-images.githubusercontent.com/11289686/35142540-ecd920ac-fcfe-11e7-991d-6716f66e5555.PNG)


**Mining example:**
Request on node 1 (:10006) 
http://localhost:10006/mine/hash

In our first mining version, we have created a proof of work algorithm that should: "Find a number that when hashed with the previous block’s solution, resulting in a hash with 4 leading 0s". The miners are then rewarded for their solution by receiving 1 coin by the network, this is stored in a transaction.

![mine](https://user-images.githubusercontent.com/11289686/35143457-e80643ea-fd01-11e7-8206-67eb1106139d.PNG)



For every succesfull mining, we add another block to the nodes copy og the blockchain, so if we do this 3 times we get an chain of 3 blocks, see the chain example.









## Sources

(1) https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

(2) https://github.com/davecan/easychain

(3) https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d

(4) https://www.oreilly.com/learning/what-is-docker-networking

(5) https://docs.docker.com/compose/compose-file/
