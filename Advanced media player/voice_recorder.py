from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtMultimedia import QMediaCaptureSession,QMediaRecorder,QAudioInput
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تسجيل الصوت")
        self.session=QMediaCaptureSession()
        self.input=QAudioInput()
        self.session.setAudioInput(self.input)
        self.recorder=QMediaRecorder()
        self.session.setRecorder(self.recorder)        
        self.حفظ=qt.QPushButton("تحديد مكان الحفظ أولا")
        self.حفظ.setDefault(True)
        self.حفظ.clicked.connect(self.opinFile)
        self.إظهار=qt.QLabel("مسار حفظ الملف")
        self.مسار=qt.QLineEdit()
        self.مسار.setReadOnly(True)
        self.مسار.setAccessibleName("مسار حفظ الملف")
        self.التسجيل=qt.QPushButton("بدء التسجيل")
        self.التسجيل.clicked.connect(self.rec)
        self.التسجيل.setDefault(True)        
        self.التسجيل.setShortcut("r")
        self.المؤقت=qt.QPushButton("الإيقاف المؤقت")
        self.المؤقت.setDefault(True)
        self.المؤقت.setDisabled(True)
        self.المؤقت.clicked.connect(self.paus)
        self.المؤقت.setShortcut("p")
        self.إيقاف=qt.QPushButton("إيقاف التسجيل")
        self.إيقاف.setDefault(True)
        self.إيقاف.setDisabled(True)
        self.إيقاف.clicked.connect(self.stop)
        self.إيقاف.setShortcut("s")                
        l=qt.QVBoxLayout(self)
        l.addWidget(self.حفظ)
        l.addWidget(self.إظهار)
        l.addWidget(self.مسار)
        l.addWidget(self.التسجيل)
        l.addWidget(self.المؤقت)
        l.addWidget(self.إيقاف)        
    def opinFile(self):
        file=qt.QFileDialog()
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
        if file.exec()==qt.QFileDialog.DialogCode.Accepted:
            self.مسار.setText(file.selectedFiles()[0])                                         
    def rec(self):
        مسار=self.مسار.text()
        if مسار:
            self.recorder.setOutputLocation(qt2.QUrl.fromLocalFile(مسار))
            self.recorder.record()
            self.التسجيل.setDisabled(True)
            self.المؤقت.setDisabled(False)
            self.إيقاف.setDisabled(False)            
        else:
            qt.QMessageBox.warning(self,"تنبيه","يرجى تحديد موقع للحفظ أولا")
    def stop(self):
        self.recorder.stop()
        self.التسجيل.setDisabled(False)
        self.إيقاف.setDisabled(True)
        self.المؤقت.setDisabled(True)
    def paus(self):
        self.recorder.pause()
        self.المؤقت.setDisabled(True)
        self.التسجيل.setDisabled(False)