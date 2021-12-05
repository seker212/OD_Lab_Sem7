from json import dumps, loads
from typing import Optional
from random import randint

from common.hasher import GetSHA256

class Block:
    prev_hash : Optional[str]
    block_hash : Optional[str]
    salt : int
    guess: Optional[int]
    data : str
    is_valid : Optional[bool] # TODO: Change to enum (valid, invalid, conflict)?
    
    def __init__(self, prev_hash: Optional[str], data: str) -> None:
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

    def validate(self) -> bool:
        """Checks if block's properties are correct.
        Change this function in order to manipulate chances to guess hash.

        Returns:
            bool: True if all properties are correct, False otherwise.
        """
        try:
            return (self.block_hash is not None and 
            self.salt is not None and
            self.guess is not None and
            self.data is not None and 
            self.salt >= 0 and
            self.salt <= 4294967295 and
            self.guess >= 0 and
            self.guess <= 4294967295 and
            GetSHA256(self.to_bytes()).hex() == self.block_hash and
            self.block_hash[0].upper() in ['A', 'B']) # This condition defines guessing chances
        except Exception as ex:
            print(ex) # TODO: Add error debug log
            return False