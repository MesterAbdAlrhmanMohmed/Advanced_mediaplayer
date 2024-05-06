from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
class photo_player(qt.QDialog):
    def __init__(self, parent,path):
        super().__init__(parent)
        self.setWindowTitle("Advanced media player")
        self.image=qt.QLabel()
        pixmap=qt1.QPixmap(path)
        self.image.setPixmap(pixmap)        
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.image)