from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from crawling import engine

def on_click_btn_start_crawling(obj):
    start_date = obj.edt_start_date.text()
    end_date = obj.edt_end_date.text()
    keyword = obj.edt_keyword.text()

    engine.start_crawling(start_date, end_date, keyword)
