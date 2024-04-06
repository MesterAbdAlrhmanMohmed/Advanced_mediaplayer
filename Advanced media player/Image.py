from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import Image_offline,Image_online
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("عرض صورة")
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.play)
        self.الخيارات.addItem("عرض صورة من الكمبيوتر")
        self.الخيارات.addItem("عرض صورة من الإنترنت")
        self.الاختيار=qt.QPushButton("إختيار")
        self.الاختيار.setShortcut("return")
        self.الاختيار.clicked.connect(self.play)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.الخيارات)
        l.addWidget(self.الاختيار)
    def play(self):
        العناصر=self.الخيارات.currentRow()
        if العناصر ==0:
            Image_offline.dialog(self).exec()
        if العناصر ==1:
            Image_online.dialog(self).exec()