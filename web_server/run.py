from flask import Flask
from flask import request
app = Flask(__name__)

import json
import datetime as date

from blockchain import block


blockchain = []
blockchain.append(block.create_genesis_block())

# Storing the transactions
nodes_transactions = []


@app.route('/transact', methods=['POST'])
def transact():
    if request.method == 'POST':
        nodes_transactions.append(request.get_json())
        return "Transaction succes"



@app.route('/mine', methods = ['POST'])
def mine():
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['proof-of-work']

  proof = block.proof_of_work(last_proof)
  req = request.get_json()

  nodes_transactions.append(
    {"from": "Pied Piper", "to": req['client'], "amount": 1}
  )
  # The data needed to create the new block
  new_block_data = {
    "proof-of-work": proof,
    "transactions": list(nodes_transactions)
  }
  new_block_index = last_block.index + 1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash

  # Empty transaction list
  nodes_transactions[:] = []

  # Create the new block!
  mined_block = block.Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)
  # Let the client know we mined a block
  return json.dumps({
      "index": new_block_index,
      "timestamp": str(new_block_timestamp),
      "data": new_block_data,
      "hash": last_block_hash
  }) + "\n"

app.run()