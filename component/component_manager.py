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

def edt_start_date(obj):
    textbox = QLineEdit(obj)
    textbox.setText('2023-01-01')
    textbox.setGeometry(cp.EDT_START_DATE_X_START, cp.EDT_START_DATE_Y_START, cp.EDT_START_DATE_WIDTH, cp.EDT_START_DATE_HEIGHT)
    return textbox

def edt_end_date(obj):
    textbox = QLineEdit(obj)
    textbox.setText('2023-01-10')
    textbox.setGeometry(cp.EDT_END_DATE_X_START, cp.EDT_END_DATE_Y_START, cp.EDT_END_DATE_WIDTH, cp.EDT_END_DATE_HEIGHT)
    return textbox

def edt_keyword(obj):
    textbox = QLineEdit(obj)
    textbox.setText('대출')
    textbox.setGeometry(cp.EDT_KEYWORD_X_START, cp.EDT_KEYWORD_Y_START, cp.EDT_KEYWORD_WIDTH, cp.EDT_KEYWORD_HEIGHT)
    return textbox
