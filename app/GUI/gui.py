# Form implementation generated from reading ui file 'od_gui.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import os, sys
from pathlib import Path
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from stylesheet import *
from gui_utils import *

CURRENT_DIRECTORY = Path(__file__).resolve().parent

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        QDir.addSearchPath("images", os.fspath(CURRENT_DIRECTORY / "images"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(mainStyle)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QSize(1200, 800))
        self.centralwidget.setMaximumSize(QSize(1200, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setMinimumSize(QSize(750, 800))
        self.left_frame.setMaximumSize(QSize(750, 800))
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.left_frame.setObjectName("left_frame")
        
        self.verticalLayout_3 = QVBoxLayout(self.left_frame)
        self.verticalLayout_3.setContentsMargins(0, 18, 0, 18)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.tableView = QTableView(self.left_frame)
        self.tableView.setMaximumSize(QSize(800, 800))
        self.tableView.setStyleSheet("")
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)

        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # header = self.tableView.verticalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        # te = QTextEdit()
        # te.setHtml("<h1><b>Block 1</b></h1><p><b>test<b></p>")
            
        # self.tableView.resizeColumnsToContents()
        # self.tableView.resizeRowsToContents()
        # data = [
        #   [te.toPlainText(),te.toPlainText(),te.toPlainText(),te.toPlainText(),te.toPlainText()],
        #   ['''START BLOCK\nHash: ''', "---", '''BLOCK 1\nHash: adada\nTimestamp: 2021-11-27''',"----",'''BLOCK 2\nHash: adada\nTimestamp: 2021-11-27'''],
        #   ['''BLOCK 3\nHash: ''', "---", '''BLOCK 4\nHash: adada\nTimestamp: 2021-11-27''',"----",'''BLOCK 5\nHash: adada\nTimestamp: 2021-11-27'''],
        #   ['''BLOCK 6\nHash: ''', "---", '''BLOCK 7\nHash: adada\nTimestamp: 2021-11-27''',"----",'''BLOCK 8\nHash: adada\nTimestamp: 2021-11-27'''],
        #   ['''BLOCK 9\nHash: ''', "---", '''BLOCK 10\nHash: adada\nTimestamp: 2021-11-27''',"----",'''BLOCK 11\nHash: adada\nTimestamp: 2021-11-27'''],
        #   ['''BLOCK 12\nHash: ''', "---", '''BLOCK 12\nHash: adada\nTimestamp: 2021-11-27''',"----",'''BLOCK 13\nHash: adada\nTimestamp: 2021-11-27'''],
        # ]
        # self.model = DataModel(data)
        # self.tableView.setModel(self.model)

        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.left_frame)
        
        self.right_frame = QFrame(self.centralwidget)
        self.right_frame.setMinimumSize(QSize(400, 800))
        self.right_frame.setMaximumSize(QSize(400, 800))
        self.right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.right_frame.setObjectName("right_frame")
        self.verticalLayout = QVBoxLayout(self.right_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.name_frame = QFrame(self.right_frame)
        self.name_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.name_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.img_name_label = QLabel(self.name_frame)
        self.img_name_label.setObjectName("img_name_label")
        self.horizontalLayout_2.addWidget(self.img_name_label)
        self.name_label = QLabel(self.name_frame)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.verticalLayout.addWidget(self.name_frame)
        
        self.add_frame = QFrame(self.right_frame)
        self.add_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.add_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.add_frame.setObjectName("add_frame")
        self.verticalLayout_2 = QVBoxLayout(self.add_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.new_frame = QFrame(self.add_frame)
        self.new_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.new_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.new_frame.setObjectName("new_frame")
        self.verticalLayout_7 = QVBoxLayout(self.new_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.add_text_field_frame = QFrame(self.new_frame)
        self.add_text_field_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.add_text_field_frame.setAutoFillBackground(False)
        self.add_text_field_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.add_text_field_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.add_text_field_frame.setObjectName("add_text_field_frame")
       
        self.horizontalLayout_7 = QHBoxLayout(self.add_text_field_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.add_label = QLabel(self.add_text_field_frame)
        self.add_label.setObjectName("add_label")
        self.horizontalLayout_7.addWidget(self.add_label)
        
        self.text_input = QLineEdit(self.add_text_field_frame)
        self.text_input.setMinimumSize(QSize(280, 30))
        self.text_input.setMaximumSize(QSize(280, 30))
        self.text_input.setText("")
        self.text_input.setObjectName("text_input")
        
        self.horizontalLayout_7.addWidget(self.text_input)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.addWidget(self.add_text_field_frame)
        
        self.add_btn = QPushButton(self.new_frame)
        self.add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_btn.setMinimumSize(QSize(120, 40))
        self.add_btn.setMaximumSize(QSize(100, 40))
        self.add_btn.setObjectName("add_btn")
        
        self.verticalLayout_7.addWidget(self.add_btn)
        self.verticalLayout_2.addWidget(self.new_frame)
        
        self.result_frame = QFrame(self.add_frame)
        self.result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.result_frame.setObjectName("result_frame")
        
        self.verticalLayout_4 = QVBoxLayout(self.result_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.result_text_field_frame = QFrame(self.result_frame)
        self.result_text_field_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.result_text_field_frame.setAutoFillBackground(False)
        self.result_text_field_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_text_field_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.result_text_field_frame.setObjectName("result_text_field_frame")
        
        self.horizontalLayout_3 = QHBoxLayout(self.result_text_field_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        self.result_label = QLabel(self.result_text_field_frame)
        self.result_label.setObjectName("result_label")
        
        self.horizontalLayout_3.addWidget(self.result_label)
        self.text_result = QLineEdit(self.result_text_field_frame)
        self.text_result.setMinimumSize(QSize(280, 30))
        self.text_result.setMaximumSize(QSize(280, 30))
        self.text_result.setText("")
        self.text_result.setObjectName("text_result")
        self.text_result.setEnabled(False)
        
        self.horizontalLayout_3.addWidget(self.text_result)
        self.verticalLayout_4.addWidget(self.result_text_field_frame)
        
        self.encryptBtn = QPushButton(self.result_frame)
        self.encryptBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.encryptBtn.setMinimumSize(QSize(120, 40))
        self.encryptBtn.setMaximumSize(QSize(100, 40))
        self.encryptBtn.setObjectName("encryptBtn")
        
        self.verticalLayout_4.addWidget(self.encryptBtn)
        self.verticalLayout_2.addWidget(self.result_frame)
        self.verticalLayout.addWidget(self.add_frame)
        
        self.bottom_frame = QFrame(self.right_frame)
        self.bottom_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
       
        self.verticalLayout_8 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.delete_btn_frame = QFrame(self.bottom_frame)
        self.delete_btn_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.delete_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.delete_btn_frame.setObjectName("delete_btn_frame")
        
        self.horizontalLayout_8 = QHBoxLayout(self.delete_btn_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        
        self.delete_btn = QPushButton(self.delete_btn_frame)
        self.delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_btn.setMinimumSize(QSize(120, 40))
        self.delete_btn.setMaximumSize(QSize(120, 40))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_8.addWidget(self.delete_btn)
        
        self.clear_btn = QPushButton(self.delete_btn_frame)
        self.clear_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setMinimumSize(QSize(120, 40))
        self.clear_btn.setMaximumSize(QSize(120, 40))
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_8.addWidget(self.clear_btn)
        
        self.verticalLayout_8.addWidget(self.delete_btn_frame)
        self.info_frame = QFrame(self.bottom_frame)
        self.info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.info_frame.setObjectName("info_frame")
        
        self.info_btn = QPushButton(self.info_frame)
        self.info_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.info_btn.setGeometry(QRect(155, 20, 155, 50))
        self.info_btn.setMinimumSize(QSize(54, 54))
        self.info_btn.setMaximumSize(QSize(54, 54))
        self.info_btn.setObjectName("info_btn")
        
        self.verticalLayout_8.addWidget(self.info_frame)
        self.verticalLayout.addWidget(self.bottom_frame)
        self.horizontalLayout.addWidget(self.right_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Method mapping
        Ui_MainWindow.set_start_block = set_start_block
        Ui_MainWindow.add_block = add_block
        Ui_MainWindow.check_text_input = check_text_input
        Ui_MainWindow.add_new_block_to_list = add_new_block_to_list
        Ui_MainWindow.set_empty_input_warning = set_empty_input_warning
        Ui_MainWindow.set_input_default_color = set_input_default_color
        Ui_MainWindow.clear_all_blocks = clear_all_blocks
        Ui_MainWindow.show_message_box = show_message_box

        # Inits
        set_start_block(self)

        # Methods mapping
        self.add_btn.clicked.connect(self.add_block)
        self.clear_btn.clicked.connect(self.clear_all_blocks)
        self.info_btn.clicked.connect(self.show_message_box)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_name_label.setText(_translate("MainWindow", ""))
        self.name_label.setText(_translate("MainWindow", "Blokchain\nModel"))
        self.add_label.setText(_translate("MainWindow", "Text:"))
        self.text_input.setPlaceholderText(_translate("MainWindow", "Type text here"))
        self.add_btn.setText(_translate("MainWindow", "Add block"))
        self.result_label.setText(_translate("MainWindow", "Result:"))
        self.encryptBtn.setText(_translate("MainWindow", "Encrypt message"))
        self.delete_btn.setText(_translate("MainWindow", "Remove block"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.info_btn.setText(_translate("MainWindow", "i"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())