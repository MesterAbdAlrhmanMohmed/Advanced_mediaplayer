from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import requests
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showFullScreen()
        self.setWindowTitle("عرض صورة من الإنترنت")
        self.الرابط=qt.QLineEdit()
        self.الرابط.setAccessibleName("إدخال رابط مباشر للصورة")
        self.عرض=qt.QPushButton("عرض الصورة")
        self.عرض.setDefault(True)
        self.عرض.clicked.connect(self.open_image_from_internet)
        self.image=qt.QLabel()
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.الرابط)
        l.addWidget(self.عرض)
        l.addWidget(self.image)
    def open_image_from_internet(self):
        try:
            text=self.الرابط.text()
            r=requests.get(text)
            pixmap=qt1.QPixmap()
            pixmap.loadFromData(r.content)
            self.image.setPixmap(pixmap)
        except:
            qt.QMessageBox.warning(self,"تحذير","فشل في الحصول على الصورة, تأكد من الإتصال بالإنترنت وتأكد بأن الرابط مباشر")