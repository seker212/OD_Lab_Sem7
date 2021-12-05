from common.block import Block
from common.hasher import GetSHA256

init_block: Block = Block(None, 'INIT')
init_block.salt = 1
init_block.block_hash = GetSHA256(init_block.salt.to_bytes(4, byteorder='big') + init_block.data.encode()).hex()
INIT_BLOCK: Block = init_block