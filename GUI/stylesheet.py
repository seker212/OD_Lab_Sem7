import os
from pathlib import Path

dir_path = os.fspath(Path(__file__).resolve().parent).replace("\\", "/")
CHAIN_IMG = dir_path + "/images/chain.png"

mainStyle = ("""QMainWindow{
    background-color: #586472;
}
QPushButton{
    background-color: #F8C830;
    border: 3px solid #fff;
    color: #000;
    border-radius: 8px;
    font-size: 14px;
}
QLineEdit{
    border: 3px solid #fff;
    background-color: #FDE2A5;
    border-radius: 8px;
    padding-left: 5px;
    color: #000;
    font-size: 15px;
}
QTableView {
    background-color: #FDE2A5;
    border: 3px solid #fff;
    border-radius: 8px;
}
QLabel{
    font-size: 15px;
    font-weight: bold;
    padding: 0;
}
#name_label{
    font-size: 45px;
}
#info_btn{
    font-size: 40px;
    background-color: #fff;
    border-radius: 26px;
    border: 2px solid #1F90D6;
}
#info_btn:hover{
    border: 2px solid #fff;
    background-color: #1F90D6;
    color: #fff;
}
#new_frame, #result_frame{
    border-top: 1px solid #fff;
}
#delete_btn_frame{
    border: 1 1 1 1;
    border-bottom: 1px solid #fff;
}
#img_name_label{
    padding-right: 30px;
    image: url(""" + CHAIN_IMG + """);
}
QPushButton:hover{
    background-color: #DB9330;
}
""")

# background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #586472, stop:1 #f8c732);}"