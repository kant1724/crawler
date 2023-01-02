from PyQt5.QtWidgets import QAction, QSizeGrip, QVBoxLayout, QWidget, QApplication, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QFont
from component import component_position as cp

def add_menu(obj):
    menubar = obj.menuBar()
    load_menu = menubar.addMenu('Load')
    excel_menu = menubar.addMenu('Excel')

def btn_start_crawling(obj):
    btn = QPushButton(obj)
    btn.setText("START CRAWLING")
    btn.setGeometry(cp.BTN_START_CRAWLING_X_START, cp.BTN_START_CRAWLING_Y_START, cp.BTN_START_CRAWLING_WIDTH, cp.BTN_START_CRAWLING_HEIGHT)
    btn.clicked.connect(obj.on_click_btn_start_crawling)

    return btn
