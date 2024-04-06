from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showFullScreen()
        self.setWindowTitle("عرض صورة من الكمبيوتر")
        self.إختيار=qt.QPushButton("إختيار صورة")
        self.إختيار.setDefault(True)
        self.إختيار.clicked.connect(self.open_image_from_file)
        self.image=qt.QLabel()
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.إختيار)
        l.addWidget(self.image)    
    def open_image_from_file(self):
        file=qt.QFileDialog(self)
        file.setAcceptMode(file.AcceptMode.AcceptOpen)
        if file.exec()==file.DialogCode.Accepted:
            pixmap=qt1.QPixmap(file.selectedFiles()[0])
            self.image.setPixmap(pixmap)