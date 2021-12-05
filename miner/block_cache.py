from typing import Optional
from common.block import Block

class ChainData:
    prev_hash: str
    block: Optional[Block]
    chain_length: int

    def __init__(self, prev_hash: str, block: Optional[Block], chain_length: int) -> None:
        self.prev_hash = prev_hash
        self.block = block
        self.chain_length = chain_length

class BlockCache:
    fake: Optional[ChainData]
    genuine: ChainData

    def __init__(self, prev_genuine_hash: str) -> None:
        self.fake = None
        self.genuine = ChainData(prev_genuine_hash, None, 1)
