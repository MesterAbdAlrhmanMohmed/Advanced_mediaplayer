from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m=QMediaPlayer()
        self.w=QAudioOutput()
        self.setWindowTitle("تشغيل صوت من الإنترنت")
        self.إظهار=qt.QLabel("إدخال رابط صوت مباشر")
        self.التعديل=qt.QLineEdit()
        self.التعديل.setAccessibleName("إدخال الرابط هنا")
        self.التعديل.setAccessibleDescription("يرجى إدخال رابط مباشر")
        self.التشغيل=qt.QPushButton("تشغيل")
        self.التشغيل.setDefault(True)
        self.التشغيل.clicked.connect(self.play)
        qt1.QShortcut("space",self).activated.connect(self.play)
        qt1.QShortcut("right",self).activated.connect(lambda: self.m.setPosition(self.m.position()+5000))
        qt1.QShortcut("left",self).activated.connect(lambda: self.m.setPosition(self.m.position()-5000))
        qt1.QShortcut("up",self).activated.connect(lambda: self.m.setPosition(self.m.position()+10000))
        qt1.QShortcut("down",self).activated.connect(lambda: self.m.setPosition(self.m.position()-10000))
        qt1.QShortcut("s",self).activated.connect(lambda: self.m.stop())
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.إظهار)
        l.addWidget(self.التعديل)
        l.addWidget(self.التشغيل)
        self.m.setAudioOutput(self.w)        
    def play(self):
        if self.التشغيل.text() == "تشغيل":
            try:
                الرابط=self.التعديل.text()
                self.التشغيل.setText("إيقاف")
                self.m.setSource(qt2.QUrl(الرابط))
                self.m.play()
            except:
                qt.QMessageBox.warning(self, "تنبيه", "يرجى إدخال رابط مباشر,ويرجى التأكد من الإتصال بالإنترنت")
        else:
            self.التشغيل.setText("تشغيل")
            self.m.stop()                