from stylesheet import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import datetime
from sys import path
from typing import Optional
import subprocess, os, psutil

if path[0].endswith('\\app'):
    del path[0]
if '' not in path:
    path.append('')

from app.receiver import Receiver
from common.init_block import INIT_BLOCK

miner_path = os.path.dirname(__file__).replace("app\GUI", "miner/miner.py")

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

    def data(self, index, role):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                value = self._data[index.row()][index.column()]
                return str(value)
            if "START" in self._data[index.row()][index.column()] and role == Qt.ItemDataRole.BackgroundRole:
                return QBrush(QColor(51, 153, 255))
            if ".VALID" in self._data[index.row()][index.column()] and role == Qt.ItemDataRole.BackgroundRole:
                return QBrush(QColor(121, 210, 166))
            if ".INVALID" in self._data[index.row()][index.column()] and role == Qt.ItemDataRole.BackgroundRole:
                return QBrush(QColor(255, 102, 102))
            if "CONFLICT" in self._data[index.row()][index.column()] and role == Qt.ItemDataRole.BackgroundRole:
                return QBrush(QColor(219, 147, 48))

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
        <p>START BLOCK<br>
        <p>Hash: {}</p>
    '''.format(list(self.blocks_dict._block_dict.values())[0][0].block_hash[:10])) #datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    self.blocks.append([te.toPlainText(),"",""])
    self.model = DataModel(self.blocks)
    self.tableView.setModel(self.model)

def refresh_blocks(self):
    block_list = list(self.worker.get_dict().values())
    if len(self.blocks) == 1 or len(self.blocks) != len(block_list):
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
    self.tableView.setModel(self.model)

def clear_all_blocks(self):
    if not (len(self.blocks) == 1 and self.blocks[0][1] == "" and self.blocks[0][2] == ""):
        self.blocks.clear()
        self.set_start_block()
    
def show_message_box(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("""<p>Program przygotowany na potrzeby realizacji projektu z przedmiotu Ochrona Danych.</p>
        <p>Zadaniem programu jest demonstracja działania blockchain oraz ataku typu 51% przy wykorzystaniu Proof of Work (PoW).</p>
        <p>Autorzy:</p>
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
    if self.is_mining == False:
        if self.workerThread.isRunning() == False:
            self.workerThread.start()
        self.process = subprocess.Popen('python {}'.format(miner_path), stdout=subprocess.PIPE, shell=True)
        self.add_btn.setText("Stop Miner")
        self.is_mining = True
    else:
        stop_miner(self)
        self.workerThread.quit()
    
def stop_miner(self):
    self.is_mining = False
    kill_process(self.process.pid)
    self.add_btn.setText("Start Miner")

def kill_process(proc_pid):
    if psutil.pid_exists(proc_pid):
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()

def clear_all(self):
    self.workerThread.quit()
    if self.process != None:
        stop_miner(self)
    self.blocks.clear()
    self.blocks.append(["","",""])
    self.model = DataModel(self.blocks)
    self.tableView.setModel(self.model)
    self.worker.reset_blockchain()
    refresh_table_content(self)
    self.workerThread.start()

def close_event(self):
    if self.process != None:
        kill_process(self.process.pid)
