from sys import path
if path[0].endswith('\\miner'):
    del path[0]
if '' not in path:
    path.append('')

from socket import socket
from random import randint
from typing import Optional
from common.block import Block
from miner.block_cache import BlockCache, ChainData
from time import sleep
from common.hasher import GetSHA256

INITIAL_BLOCK_HASH: str = 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb' #FIXME: Change initial block hash
MAX_FAKE_FALLBEHIND: int = 5
FAKE_MIMERS_COUNT: int = 2
GENUINE_MINERS_COUNT: int = 3
SLEEP_SECONDS: int = 5
FAKE_MINERS_DELAY_COUNT: int = 2


class Miner:
    def __init__(self) -> None:
        self._block_cache = BlockCache(INITIAL_BLOCK_HASH)
        self.front_socket: socket = socket()
        self.front_socket.connect(('localhost', 30000))

    def _guess(self, block: Block) -> bool:
        block.guess = randint(0, 4294967295)
        block.block_hash = GetSHA256(block.to_bytes()).hex()
        if block.validate():
            return True
        else:
            block.guess = None
            block.block_hash = None
            return False
        
    def _produce(self, is_fake: bool) -> None:
        if is_fake:
            new_block: Optional[Block] = None
            if self._block_cache.fake is not None and self._block_cache.genuine.chain_length - self._block_cache.fake.chain_length <= MAX_FAKE_FALLBEHIND:
                if self._block_cache.fake.block is not None:
                    self._block_cache.fake.prev_hash = self._block_cache.fake.block.block_hash
                new_block = Block(self._block_cache.fake.prev_hash, 'FAKE')
            else:
                new_block = Block(self._block_cache.genuine.prev_hash, 'FAKE')
            self._block_cache.fake.block = new_block
        else:
            if self._block_cache.genuine.block is not None:
                self._block_cache.genuine.prev_hash = self._block_cache.genuine.block.block_hash
            self._block_cache.genuine.block = Block(self._block_cache.genuine.prev_hash, 'GENUINE')

    def _send(self, block: Block):
        self.front_socket.send(block.to_json().encode('ascii'))
        sleep(0.1)

    def mine(self):
        while True:
            for thread_num in range(FAKE_MIMERS_COUNT + GENUINE_MINERS_COUNT):
                if thread_num < GENUINE_MINERS_COUNT:
                    # Simulate genuine miner
                    if self._block_cache.genuine.block is None:
                        self._produce(False)
                    if self._guess(self._block_cache.genuine.block):
                        self._send(self._block_cache.genuine.block)
                        self._produce(False)
                else:
                    # Simulate fake miner
                    if self._block_cache.genuine.chain_length < FAKE_MINERS_DELAY_COUNT:
                        if self._block_cache.fake is None:
                            self._block_cache.fake = ChainData(self._block_cache.genuine.prev_hash, None, self._block_cache.genuine.chain_length)
                            self._produce(True)
                        if self._guess(self._block_cache.fake.block):
                            self._send(self._block_cache.fake.block)
                            self._produce(True)

            sleep(SLEEP_SECONDS)

if __name__ == '__main__':
    miner = Miner()
    miner.mine()