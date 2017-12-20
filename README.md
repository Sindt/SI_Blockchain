# Blockchain 
### Christian Sindt, Kasper Pontoppidan & Kasper Olesen 


## The application 

SomeText about the current state of the application

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


## How to run

SomeText about how to run the application (bash scripts etc.)



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


