from sys import path
from typing import Optional
if path[0].endswith('\\app'):
    del path[0]
if '' not in path:
    path.append('')

from socket import socket
from common.block import Block 
from app.block_chain import BlockChain
from common.init_block import INIT_BLOCK

class Receiver:
    block_chain: BlockChain

    def __init__(self) -> None:        
        self.block_chain = BlockChain(INIT_BLOCK)

        self._miner_socket: socket = socket()
        # self._miner_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._miner_socket.bind(('localhost', 30000))
        self._miner_conn: Optional[socket] = None

    def start_connection(self):
        self._miner_socket.listen()
        self._miner_conn, _ = self._miner_socket.accept()
        while True:
            print("fuck")
            msg = self._miner_conn.recv(4096)
            block = Block.from_json(msg.decode('ascii'))
            if block.validate():
                self.block_chain.append(block)
                self.block_chain.validate_chain()

if __name__ == '__main__':
    receiver = Receiver()
    receiver.start_connection()