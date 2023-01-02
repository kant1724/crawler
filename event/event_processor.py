from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from crawling import engine

def on_click_btn_start_crawling(obj):
    engine.start()
