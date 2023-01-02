import sys
import keyboard
from PyQt5.QtWidgets import QSizeGrip, QVBoxLayout, QWidget, QApplication, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt, QSettings
#from gui_control import control
from component import component_manager as cm
#from engine import event_processor as ep
#from engine import execution

class layout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        cm.add_menu(self)
        self.btn_start_crawling = cm.btn_start_crawling(self)
        self.setGeometry(300, 300, 800, 450)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    layout = layout()
    sys.exit(app.exec_())