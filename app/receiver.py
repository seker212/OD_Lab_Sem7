from sys import path
from typing import Optional
if path[0].endswith('\\app'):
    del path[0]
if '' not in path:
    path.append('')

from socket import socket
from common.block import Block 
from app.block_chain import BlockChain
from miner.miner import INITIAL_BLOCK_HASH #FIXME: Initial block should be in "common" package

class Receiver:
    block_chain: BlockChain

    def __init__(self) -> None:
        #FIXME: Create legit initial block with proper hash
        init_block = Block(None, 'INIT')
        init_block.block_hash = INITIAL_BLOCK_HASH
        
        self.block_chain = BlockChain(init_block)

        self._miner_socket: socket = socket()
        self._miner_socket.bind(('localhost', 30000))
        self._miner_conn: Optional[socket] = None

    def start_connection(self):
        self._miner_socket.listen()
        self._miner_conn, _ = self._miner_socket.accept()
        while True:
            msg = self._miner_conn.recv(4096)
            block = Block.from_json(msg.decode('ascii'))
            if block.validate():
                self.block_chain.append(block)
                self.block_chain.validate_chain()
            # print('\n\n================================')
            # for x in self.block_chain._block_dict.values():
            #     print(x[0].to_json())
            # print('================================')

if __name__ == '__main__':
    receiver = Receiver()
    receiver.start_connection()