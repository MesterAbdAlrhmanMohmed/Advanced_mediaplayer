from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import os
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)        
        self.showFullScreen()
        self.m=QMediaPlayer()
        self.w=QAudioOutput()
        self.vw=QVideoWidget()        
        self.m.setVideoOutput(self.vw)
        self.setWindowTitle("فتح مجلد يحتوي على فيديوهات وصوتيات")
        self.فتح=qt.QPushButton("فتح مجلد")
        self.فتح.setDefault(True)
        self.فتح.clicked.connect(self.opinFile)        
        self.التعديل=qt.QLineEdit()
        self.التعديل.setReadOnly(True)
        self.التعديل.setAccessibleName("مسار المجلد")
        self.القائمة=qt.QComboBox()        
        self.تشغيل=qt.QPushButton("تشغيل")
        self.تشغيل.setDefault(True)
        self.تشغيل.clicked.connect(self.play)        
        qt1.QShortcut("space",self).activated.connect(lambda: self.m.pause())
        qt1.QShortcut("r",self).activated.connect(lambda: self.m.play())        
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
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.فتح)
        l.addWidget(self.التعديل)
        l.addWidget(self.القائمة)
        l.addWidget(self.vw)
        l.addWidget(self.تشغيل)
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
    def opinFile(self):
        file = qt.QFileDialog()
        file.setFileMode(qt.QFileDialog.FileMode.Directory)
        if file.exec() == qt.QFileDialog.DialogCode.Accepted:
            folder_path=file.selectedFiles()[0]            
            self.التعديل.setText(folder_path)  # تحديث مربع النص بالمسار الكامل للمجلد
            self.القائمة.clear()  # مسح قائمة العناصر الحالية
            self.القائمة.addItem("محتوا المجلد")
            audio_formats=['.mp3', '.wav', '.wma', '.aac', '.m4a', '.flac', '.ogg', '.opus', '.ape', '.mpga', '.alac', '.wv', '.mka','.aiff','.au','.dss','.iff','.m4r']
            video_formats=['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.3gp', '.webm', '.rm', '.m2ts', '.vob', '.mts', '.mxf','.SWF','.AV1','.VP9']
            image_formats=['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.ai', '.raw', '.svg', '.heic', '.webp', '.ps','.EPS','.PCT','.TGA','.FITS','.JP2']
            for file_name in os.listdir(folder_path):
                if any(file_name.endswith(format) for format in (*audio_formats, *video_formats)):
                    self.القائمة.addItem(file_name)
    def play(self):
        if not self.القائمة.currentIndex():
            return        
        file_name=self.القائمة.currentText()
        folder_path=self.التعديل.text()
        file_path=os.path.join(folder_path, file_name)                
        video_formats=['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.3gp', '.webm', '.rm', '.m2ts', '.vob', '.mts', '.mxf']
        audio_formats=['.mp3', '.wav', '.wma', '.aac', '.m4a', '.flac', '.ogg', '.opus', '.ape', '.mpga', '.alac', '.wv', '.mka']
        self.m.setSource(qt2.QUrl.fromLocalFile(file_path))            
        if os.path.isfile(file_path) and any(file_path.endswith(format) for format in (*video_formats, *audio_formats)):
            if self.m.isPlaying():
                self.m.pause()    
                self.تشغيل.setText("تشغيل")
            else:                
                self.m.play()
                self.تشغيل.setText("إيقاف مؤقت")            
        else:
            qt.QMessageBox.warning(self, "تنبيه", "يرجى تحديد ملف فيديو أو صوت  صالح للتشغيل")