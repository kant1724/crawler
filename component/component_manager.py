from PyQt5.QtWidgets import QAction, QSizeGrip, QVBoxLayout, QWidget, QApplication, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QFont

def add_menu(obj):
    menubar = obj.menuBar()
    load_menu = menubar.addMenu('Load')
    excel_menu = menubar.addMenu('Excel')
