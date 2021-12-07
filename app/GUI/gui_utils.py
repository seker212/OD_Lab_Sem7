from stylesheet import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import datetime
from sys import path
from typing import Optional
from subprocess import Popen
import os
if path[0].endswith('\\app'):
    del path[0]
if '' not in path:
    path.append('')

from app.receiver import Receiver
from common.init_block import INIT_BLOCK

miner_path = os.path.dirname(__file__).replace("app\GUI", "miner/miner.py")

# blocks = []
# reciver = Receiver()
current_lenght = 0

class DataModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self._data[index.row()][index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()][index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

def set_start_block(self):
    te = QTextEdit()
    te.setText('''
        START BLOCK
        Hash: {}
    '''.format(list(self.blocks_dict._block_dict.values())[0][0].block_hash[:10])) #datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    self.blocks.append([te.toPlainText(),"",""])
    self.model = DataModel(self.blocks)
    self.tableView.setModel(self.model)

# def add_block(self):
#     if not self.check_text_input():
#         self.set_empty_input_warning()
#     else:
#         self.set_input_default_color()
#         self.add_new_block_to_list()

def refresh_blocks(self):
    block_list = list(self.worker.get_dict().values())
    if len(self.blocks) != len(block_list):
        self.blocks.clear()
        add_new_blocks_to_list(self, block_list)

def add_new_blocks_to_list(self, blocks_list):
    for i, b in enumerate(blocks_list):
        if i == 0:
            te = QTextEdit()
            te.setText('''
                START BLOCK
                Hash: {}
                Data: {}
                Is valid: {} 
            '''.format(b[0].block_hash[:10], b[0].data, b[0].is_valid))
        else:
            te = QTextEdit()
            te.setText('''
                BLOCK {}
                Hash: {}
                Prev Hash: {}
                Data: {}
                {}
            '''.format(i, b[0].block_hash[:10], b[0].prev_hash[:10], b[0].data, b[0].is_valid))
        
        if "Hash: " + b[0].block_hash[:10] not in self.blocks:
            if not any("" in block for block in self.blocks):
                self.blocks.append([te.toPlainText(),"",""])
            else:   
                for r in range(len(self.blocks)):
                    for c in range(3):
                        if self.blocks[r][c] == "":
                            self.blocks[r][c] = te.toPlainText()
                            break
   

def refresh_table_content(self):
    refresh_blocks(self)
    self.model = DataModel(self.blocks)
    self.model.setbackgroundcolor(0, 0, value:QColr)
    self.tableView.setModel(self.model)

def clear_all_blocks(self):
    if not (len(self.blocks) == 1 and self.blocks[0][1] == "" and self.blocks[0][2] == ""):
        self.blocks.clear()
        self.set_start_block()
    
def show_message_box(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("""<p>Program przygotowany na potrzeby realizacji projektu z przedmiotu Ochrona Danych.</p>
        <p>Zadaniem programu jest demonstracja działania blockchain</p>
        <ul>
            <li>Sebastian Skrobich</li>
            <li>Karol Sienkiewicz</li>
            <li>Piotr Sobieraj</li>
            <li>Eryk Wittchen</li>
        </ul>
        <p>Wersja: 1.0</p>
        """)
        msgBox.setWindowTitle("Info")
        msgBox.setStyleSheet(infoStyle)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.buttons()[0].setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        msgBox.exec()

def run_miner(self):
    Popen('python {}'.format(miner_path))
    # os.system("cmd /c python miner/miner.py") 

def clear_all(self):
    self.workerThread.terminate()
    self.blocks.clear()
    self.blocks.append(["","",""])
    self.model = DataModel(self.blocks)
    self.tableView.setModel(self.model)

# def interval_refresh_blocks(self):
#      # timer which repate function `display_time` every 1000ms (1s)
#     timer = QTimer()
#     timer.timeout.connect(refresh_table_content)  # execute `display_time`
#     timer.setInterval(1000)  # 1000ms = 1s
#     timer.start()
