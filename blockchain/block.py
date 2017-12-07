import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.prev_hash).encode('utf-8'))
                   #.join(self.timestamp).join(self.data).join(self.prev_hash))
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), {
        "proof-of-work": 7,
        "transactions": None
    }, "0000")


def proof_of_work(last_proof):
  incrementor = last_proof + 1
  # Keep incrementing until it's equal to a number divisible by 7
  #  AND the proof of work of the previous block in the chain(First time == 8)
  while not (incrementor % 7 == 0 and incrementor % last_proof == 0):
    incrementor += 1

  return incrementor