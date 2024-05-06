from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
class player(qt.QDialog):
    def __init__(self, parent, path):
        super().__init__(parent)
        self.setWindowTitle("advanced media player")
        self.m=QMediaPlayer()
        self.w=QAudioOutput()
        self.vw=QVideoWidget()        
        self.m.setVideoOutput(self.vw)
        self.m.setSource(qt2.QUrl.fromLocalFile(path))
        self.m.play()
        self.showFullScreen()
        self.المدة=qt.QLineEdit()
        self.المدة.setReadOnly(True)        
        self.المدة.setAccessibleName("مدة المقطع")
        self.التقدم = qt.QSlider(qt2.Qt.Orientation.Horizontal)
        self.التقدم.setRange(0,100)
        self.التقدم.setAccessibleName("االوقت المنقضي")
        self.m.durationChanged.connect(self.update_slider)
        self.m.positionChanged.connect(self.update_slider)
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
        l.addWidget(self.vw)        
        l.addWidget(self.المدة)
        l.addWidget(self.التقدم)
        self.m.setAudioOutput(self.w)        
    def play(self):
        if self.m.isPlaying():
            self.m.pause()
        else:
            self.m.play()    
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
    def increase_volume(self):
        current_volume=self.w.volume()
        new_volume=current_volume+0.10
        self.w.setVolume(new_volume)
    def decrease_volume(self):
        current_volume=self.w.volume()
        new_volume=current_volume-0.10
        self.w.setVolume(new_volume)
    def update_slider(self):
        self.التقدم.setValue(int((self.m.position()/self.m.duration())*100))        
        self.time_VA()
    def time_VA(self):
        position = self.m.position()
        duration = self.m.duration()
        duration_str = qt2.QTime(0, (duration // 60000) % 60, (duration // 1000) % 60, duration % 1000).toString()
        position_str = qt2.QTime(0, (position // 60000) % 60, (position // 1000) % 60, position % 1000).toString()
        self.المدة.setText(f"الوقت المنقضي: {position_str}، مدة المقطع: {duration_str}")