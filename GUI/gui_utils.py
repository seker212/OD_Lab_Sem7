from stylesheet import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import datetime

blocks = []

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
        Hash: H5fgSF
        TimeStamp: {}
    '''.format(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
    blocks.append([te.toPlainText(),"",""])
    self.model = DataModel(blocks)
    self.tableView.setModel(self.model)

def add_block(self):
    if self.check_if_text_is_empty():
        self.text_input.setText("Please fill this field.")
    else:
        self.add_new_block_to_list()


def add_new_block_to_list(self):
    te = QTextEdit()
    te.setText('''
        BLOCK
        Hash: H5fgSF
        Prev Hash: JKd78HH
        TimeStamp: {}
        Message: {}
    '''.format(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), self.text_input.text()))
    print(blocks)
    
    if not any("" in block for block in blocks):
        blocks.append([te.toPlainText(),"",""])
    else:   
        for r in range(len(blocks)):
            for c in range(3):
                if blocks[r][c] == "":
                    blocks[r][c] = te.toPlainText()
                    break
            
    self.model = DataModel(blocks)
    self.tableView.setModel(self.model)

def check_if_text_is_empty(self):
    if self.text_input.text() == "":
        return True
    else:
        return False
