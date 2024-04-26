from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import folder_Audio,folder_Image,folder_Video,folder_all
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("فتح مجلد")
        self.القائمة=qt.QListWidget()
        self.القائمة.clicked.connect(self.s)
        self.القائمة.addItem("الصوتيات")
        self.القائمة.addItem("الفيديوهات")
        self.القائمة.addItem("الصور")
        self.القائمة.addItem("فتح مجلد يحتوي على فيديوهات وصوتيات")
        qt1.QShortcut("return",self).activated.connect(self.s)
        self.تنبيه=qt.QLineEdit()
        self.تنبيه.setReadOnly(True)
        self.تنبيه.setAccessibleName("تنبيه هام")
        self.تنبيه.setText("للإيقاف المؤقت نضغط مسافة وللإستئناف نضغط حرف R")
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.القائمة)
        l.addWidget(self.تنبيه)        
    def s(self):
        العناصر=self.القائمة.currentRow()
        if العناصر==0:
            folder_Audio.dialog(self).exec()
        if العناصر==1:
            folder_Video.dialog(self).exec()
        if العناصر==2:
            folder_Image.dialog(self).exec()
        if العناصر==3:
            folder_all.dialog(self).exec()