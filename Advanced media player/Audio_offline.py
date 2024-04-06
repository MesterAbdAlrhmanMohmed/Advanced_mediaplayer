from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m=QMediaPlayer()
        self.w=QAudioOutput()
        self.setWindowTitle("تشغيل صوت من الكمبيوتر")
        self.فتح=qt.QPushButton("فتح ملف o")
        self.فتح.setDefault(True)
        self.فتح.setShortcut("o")
        self.فتح.clicked.connect(self.opinFile)
        self.إظهار=qt.QLabel("مسار الملف")
        self.التعديل=qt.QLineEdit()
        self.التعديل.setAccessibleName("مسار الملف")        
        self.التعديل.setReadOnly(True)
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
        l.addWidget(self.فتح)
        l.addWidget(self.إظهار)
        l.addWidget(self.التعديل)
        l.addWidget(self.التشغيل)
        self.m.setAudioOutput(self.w)        
    def play(self):
        if self.m.isPlaying():
            self.m.pause()
            self.التشغيل.setText("تشغيل")
        else:
            self.m.play()
            self.التشغيل.setText("إيقاف مؤقت")
    def opinFile(self):
        file=qt.QFileDialog()
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
        if file.exec()==qt.QFileDialog.DialogCode.Accepted:
            self.التعديل.setText(file.selectedFiles()[0])                                 
            self.m.setSource(qt2.QUrl.fromLocalFile(self.التعديل.text()))
            self.m.play()
            self.التشغيل.setText("إيقاف مؤقت")        