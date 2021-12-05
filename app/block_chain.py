from typing import Dict, List, Tuple
from common.block import Block
from common.block_status import BlockStatus

class BlockChain:
    def __init__(self, starting_block: Block) -> None:
        starting_block.is_valid = True
        self._block_dict: Dict[str, Tuple[Block, int]] = { starting_block.block_hash : (starting_block, 1) } # { block_hash -> (block, chain_length) }
        self._max_len: int = 1
        self._starting_hash: str = starting_block.block_hash

    def append(self, block: Block) -> None:
        new_len = self._block_dict[block.prev_hash][1] + 1
        self._block_dict[block.block_hash] = (block, new_len)        

        if new_len > self._max_len:
            self._max_len = new_len

    def validate_chain(self) -> None:
        """Validates blocks based on PoW by setting each block's `is_valid` property"""
        last_nodes = []
        for value in self._block_dict.values():
            if value[0].block_hash != self._starting_hash:
                value[0].is_valid = BlockStatus.INVALID
            if value[1] == self._max_len:
                last_nodes.append(value[0].block_hash)
        for hash in last_nodes:
            current_hash = hash
            while current_hash != self._starting_hash:
                block = self._block_dict[current_hash][0]
                if len(last_nodes) == 1:
                    block.is_valid = BlockStatus.VALID
                else:
                    block.is_valid = BlockStatus.CONFLICT
                current_hash = block.prev_hash
