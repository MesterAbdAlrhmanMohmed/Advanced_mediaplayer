from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from pytube import YouTube
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m=QMediaPlayer()
        self.w=QAudioOutput()
        self.vw=QVideoWidget()        
        self.m.setVideoOutput(self.vw)
        self.showFullScreen()
        self.setWindowTitle("تشغيل فيديو من الإنترنت")        
        self.نوع=qt.QComboBox()
        self.نوع.addItem("تشغيل فيديو من youtube")
        self.نوع.addItem("تشغيل فيديو من رابط مباشر")
        self.نوع.setAccessibleName("نوع الفيديو")
        self.التعديل=qt.QLineEdit()
        self.التعديل.setAccessibleName("رابط الفيديو")        
        self.التشغيل=qt.QPushButton("تشغيل")
        self.التشغيل.setDefault(True)
        self.التشغيل.clicked.connect(self.play_b)
        qt1.QShortcut("space",self).activated.connect(self.play)
        qt1.QShortcut("right",self).activated.connect(lambda: self.m.setPosition(self.m.position()+5000))
        qt1.QShortcut("left",self).activated.connect(lambda: self.m.setPosition(self.m.position()-5000))
        qt1.QShortcut("up",self).activated.connect(lambda: self.m.setPosition(self.m.position()+10000))
        qt1.QShortcut("down",self).activated.connect(lambda: self.m.setPosition(self.m.position()-10000))
        qt1.QShortcut("s",self).activated.connect(lambda: self.m.stop())
        l=qt.QVBoxLayout(self)                                    
        l.addWidget(self.نوع)
        l.addWidget(self.التعديل)
        l.addWidget(self.vw)
        l.addWidget(self.التشغيل)
        self.m.setAudioOutput(self.w)        
    def play_b(self):
        try:
            النوع=self.نوع.currentIndex()
            if النوع ==0:
                الفيديو=YouTube(self.التعديل.text())
                stream=الفيديو.streams.get_highest_resolution()
                self.m.setSource(qt2.QUrl(stream.url))
            if النوع ==1:
                self.m.setSource(qt2.QUrl(self.التعديل.text()))
            self.m.play()        
        except:
            qt.QMessageBox.warning(self,"تنبيه","يرجى إدخال رابط صحيح أو التأكد من الإتصال بالإنترنت")
    def play(self):
        if self.m.isPlaying():
            self.m.pause()
            self.التشغيل.setText("تشغيل")
        else:
            self.m.play()
            self.التشغيل.setText("إيقاف مؤقت")