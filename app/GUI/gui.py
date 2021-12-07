import os, sys, time
from pathlib import Path
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from stylesheet import *
from gui_utils import *
from app.block_chain import BlockChain

CURRENT_DIRECTORY = Path(__file__).resolve().parent

class WorkerThread(QObject):
    signalExample = pyqtSignal(str, int)
 
    def __init__(self):
        super().__init__()
        self.reciver = Receiver() 
    
    def get_dict(self):
        return self.reciver.block_chain._block_dict
    
    def reset_blockchain(self):
        self.reciver.block_chain = BlockChain(INIT_BLOCK)
 
    @pyqtSlot()
    def run(self):
        self.reciver.start_connection()

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
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

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
        self.verticalLayout_7 = QHBoxLayout(self.new_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.add_text_field_frame = QFrame(self.new_frame)
        self.add_text_field_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.add_text_field_frame.setAutoFillBackground(False)
        self.add_text_field_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.add_text_field_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.add_text_field_frame.setObjectName("add_text_field_frame")
        
        self.add_btn = QPushButton(self.new_frame)
        self.add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_btn.setMinimumSize(QSize(120, 40))
        self.add_btn.setMaximumSize(QSize(100, 40))
        self.add_btn.setObjectName("add_btn")
        
        self.verticalLayout_7.addWidget(self.add_btn)
        self.verticalLayout_2.addWidget(self.new_frame)
        
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

        self.worker = WorkerThread()
        self.workerThread = QThread()
        self.workerThread.started.connect(self.worker.run)  # Init worker run() at startup (optional)
        self.worker.signalExample.connect(self.signalExample)  # Connect your signals/slots
        self.worker.moveToThread(self.workerThread)  # Move the Worker object to the Thread object
        self.workerThread.start()
    
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Fields
        self.blocks = []
        self.process = None
        self.is_mining = False
        self.clear_flag = False

        # Method mapping
        Ui_MainWindow.set_start_block = set_start_block
        Ui_MainWindow.add_new_blocks_to_list = add_new_blocks_to_list
        Ui_MainWindow.refresh_blocks = refresh_blocks
        Ui_MainWindow.refresh_table_content = refresh_table_content
        Ui_MainWindow.clear_all_blocks = clear_all_blocks
        Ui_MainWindow.show_message_box = show_message_box
        Ui_MainWindow.run_miner = run_miner
        Ui_MainWindow.clear_all = clear_all
        Ui_MainWindow.close_event = close_event

        # Inits
        refresh_blocks(self)

        # Methods mapping
        self.add_btn.clicked.connect(self.run_miner)
        self.clear_btn.clicked.connect(self.clear_all)
        self.info_btn.clicked.connect(self.show_message_box)
        app.aboutToQuit.connect(self.close_event)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_name_label.setText(_translate("MainWindow", ""))
        self.name_label.setText(_translate("MainWindow", "Blokchain\nModel"))
        self.add_btn.setText(_translate("MainWindow", "Run Miner"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.info_btn.setText(_translate("MainWindow", "i"))
    
    def signalExample(self, text, number):
        print(text)
        print(number)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    timer = QTimer()
    timer.timeout.connect(ui.refresh_table_content)  # execute `display_time`
    # timer.setInterval(100)  # 1000ms = 1s
    timer.start()

    sys.exit(app.exec())
