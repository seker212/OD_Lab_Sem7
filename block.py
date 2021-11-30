from datetime import datetime
from random import randbytes

class Block:
    prev_hash : str
    block_hash : str
    time_stamp : datetime
    salt : str
    data : str

    def __init__(self, prev_hash:str, data:str) -> None:
        self.prev_hash = prev_hash
        self.block_hash = None
        self.time_stamp = datetime.now()
        self.salt = randbytes(32).hex()
        self.data = data

    def get_byets(self): #FIXME: add datetime conversion
        return bytes.fromhex(self.prev_hash) + bytes.fromhex(self.salt) + self.data.encode()