from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import Video_offline,Video_online
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تشغيل فيديو")
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.play)
        self.الخيارات.addItem("تشغيل فيديو من الكمبيوتر")
        self.الخيارات.addItem("تشغيل فيديو من الإنترنت")
        qt1.QShortcut("return",self).activated.connect(self.play)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.الخيارات)        
    def play(self):
        العناصر=self.الخيارات.currentRow()
        if العناصر ==0:
            Video_offline.dialog(self).exec()
        if العناصر ==1:
            Video_online.dialog(self).exec()