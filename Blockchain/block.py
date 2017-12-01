import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hasher.sha256()
        sha.update(' '.join(self.index,self.timestamp,self.data,self.prev_hash))
        return sha.hexdigest()


