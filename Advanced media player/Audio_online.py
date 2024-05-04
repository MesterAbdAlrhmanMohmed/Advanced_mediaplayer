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
        qt1.QShortcut("ctrl+right",self).activated.connect(lambda: self.m.setPosition(self.m.position()+30000))
        qt1.QShortcut("ctrl+left",self).activated.connect(lambda: self.m.setPosition(self.m.position()-30000))
        qt1.QShortcut("ctrl+up",self).activated.connect(lambda: self.m.setPosition(self.m.position()+60000))
        qt1.QShortcut("ctrl+down",self).activated.connect(lambda: self.m.setPosition(self.m.position()-60000))
        qt1.QShortcut("s",self).activated.connect(lambda: self.m.stop())
        qt1.QShortcut("ctrl+1",self).activated.connect(self.t10)
        qt1.QShortcut("ctrl+2",self).activated.connect(self.t20)
        qt1.QShortcut("ctrl+3",self).activated.connect(self.t30)
        qt1.QShortcut("ctrl+4",self).activated.connect(self.t40)
        qt1.QShortcut("ctrl+5",self).activated.connect(self.t50)
        qt1.QShortcut("ctrl+6",self).activated.connect(self.t60)
        qt1.QShortcut("ctrl+7",self).activated.connect(self.t70)
        qt1.QShortcut("ctrl+8",self).activated.connect(self.t80)
        qt1.QShortcut("ctrl+9",self).activated.connect(self.t90)
        qt1.QShortcut("shift+up",self).activated.connect(self.increase_volume)
        qt1.QShortcut("shift+down",self).activated.connect(self.decrease_volume)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.إظهار)
        l.addWidget(self.التعديل)
        l.addWidget(self.التشغيل)
        self.m.setAudioOutput(self.w)        
    def t10(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.1))
    def t20(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.2))
    def t30(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.3))
    def t40(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.4))
    def t50(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.5))
    def t60(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.6))
    def t70(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.7))
    def t80(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.8))
    def t90(self): 
        total_duration = self.m.duration()
        self.m.setPosition(int(total_duration * 0.9))    
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
    def increase_volume(self):
        current_volume=self.w.volume()
        new_volume=current_volume+0.10
        self.w.setVolume(new_volume)
    def decrease_volume(self):
        current_volume=self.w.volume()
        new_volume=current_volume-0.10
        self.w.setVolume(new_volume)