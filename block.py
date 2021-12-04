from json import dumps, loads
from typing import Optional
from random import randint

class Block:
    prev_hash : str
    block_hash : Optional[str]
    salt : int
    guess: Optional[int]
    data : str
    is_valid : Optional[bool]
    
    def __init__(self, prev_hash:str, data:str) -> None:
        self.prev_hash = prev_hash
        self.block_hash = None
        self.salt = randint(0, 4294967295)
        self.data = data
        self.guess = None
        self.is_valid = None

    @classmethod
    def from_json(cls, json):
        tmp = cls('', '')
        tmp.__dict__ = loads(json)
        return tmp

    def to_bytes(self) -> bytes:
        return bytes.fromhex(self.prev_hash) + self.salt.to_bytes(4, byteorder='big') + self.guess.to_bytes(4, byteorder='big') + self.data.encode()
    
    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__)