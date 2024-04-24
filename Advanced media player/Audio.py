from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import Audio_offline, Audio_online
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تشغيل صوت")
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.play)
        self.الخيارات.addItem("تشغيل صوت من الكمبيوتر")
        self.الخيارات.addItem("تشغيل صوت من الإنترنت")
        qt1.QShortcut("return",self).activated.connect(self.play)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.الخيارات)        
    def play(self):
        العناصر=self.الخيارات.currentRow()
        if العناصر ==0:
            Audio_offline.dialog(self).exec()
        if العناصر ==1:
            Audio_online.dialog(self).exec()