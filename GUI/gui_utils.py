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
    if not self.check_text_input():
        self.set_empty_input_warning()
    else:
        self.set_input_default_color()
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

def check_text_input(self):
    if self.text_input.text() == "" or "Please fill this field!" in self.text_input.text():
        return False
    else:
        return True
    
def set_empty_input_warning(self):
    self.text_input.setStyleSheet("color: #ff0000")
    self.text_input.setText("Please fill this field!")

def set_input_default_color(self):
    self.text_input.setStyleSheet("color: #00000")

def clear_all_blocks(self):
    if not (len(blocks) == 1 and blocks[0][1] == "" and blocks[0][2] == ""):
        blocks.clear()
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
