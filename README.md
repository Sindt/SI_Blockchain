# Blockchain 
### Christian Sindt, Kasper Pontoppidan & Kasper Olesen 


## The application 

This shows the parts of our system that managed to get developed successfully. we did not complete all of the assignment in time, see futher explanation under "How to run".

At the moment our system consists of 2 python files in the /blockchain folder:
``` python
block.py - Our blockchain

p2p.py - Our Peer-to-Peer network
```

The application will run by default on localhost:5000

### Endpoints

GET - nodes/mine

GET - nodes/chain

POST - nodes/transactions/new 

Transaction structure:

```
{
	"sender": "someValue",

	"recipient": "someOtherValue"

	"amount": someNumber
}
```

POST - nodes/register

GET - nodes/resolve

### Mining example:
```
http://localhost:5000/mine

Response:
```
![mine](https://user-images.githubusercontent.com/11289686/34226747-f785cafa-e5ca-11e7-9a35-d379d4a69d43.PNG)

For every mining, we add another block to the chain, so if we do this 3 times we get an chain of 3 blocks, see the chain example.

### Chain example:
```
http://localhost:5000/chain

Response:
```
![chain](https://user-images.githubusercontent.com/11289686/34227171-88f01698-e5cc-11e7-92db-620df0df57a6.PNG)



### Peer-to-Peer example:
This is an example of how our peer-to-peer network are working:
![p2p1](https://i.imgur.com/RfhHh7hr.png)

After closing the server it automatically finds a new one among the nodes:
![p2p2](https://user-images.githubusercontent.com/11289686/34229671-7179d1d0-e5d5-11e7-8853-531586ccdd81.PNG)



## How to run
**NB!:**
Vi havde mange udfordringer med vores peer-to-peer netværk og docker-swarm (som vi endte med at måtte droppe at bruge), dette gjorde at vi ikke fik vores system ”samlet” inden afleveringsfristen.

Vi fik lavet det meste af vores blockchain og dens funktionalitet.

Vi fik lavet en stor del af vores P2P netværk.

Vi fik konfigureret 4 docker containers, ved hjælp docker-compose, som hver især kan kører vores blockchain.

Men vi fik IKKE lavet vores blockchain, som en del af vores p2p netværk, endnu. 

Nedenfor er er beskrivelse af hvordan man installere og kører de forskellige komponenter, når de rent faktisk er udviklet færdigt. Derfor er det ikke alle delene af "guiden" som pt. vil virke.

**How to run:**
Our system depends on Docker and Docker-compose. To install, run:
``` $$bash
bash install.sh

```

To start our blockchain application run:
``` $$bash
bash run.sh

```
This will run the docker-compose file, (in the root of the repository) and start up 4 containers running the block.py serivce.

Example:
![nodes](https://user-images.githubusercontent.com/11289686/34226638-9a4c9af8-e5ca-11e7-9898-0d51c77d6370.PNG)

4 containers running:
![containers](https://user-images.githubusercontent.com/11289686/34228634-9e405288-e5d1-11e7-8e41-33e5a45dccf3.PNG)


## Sources
As we had a really hard time creating our blockchain in python, we had to get help and inspiration
from various different sources on the internet:

(1) https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

This source has been used as our go-to guide in creating the blockchain, which also means that 
we have borrowed heavily from this guide.

(2) https://github.com/davecan/easychain

This source has helped guide us and understand the concept of a blockchain in python

(3) https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d

(4) https://www.oreilly.com/learning/what-is-docker-networking

(5) https://docs.docker.com/compose/compose-file/

(6) https://blog.codeship.com/docker-machine-compose-and-swarm-how-they-work-together/

(7) https://www.youtube.com/watch?v=Rvfs6Xx3Kww
