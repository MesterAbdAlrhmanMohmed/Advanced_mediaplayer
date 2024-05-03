from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import photo_shoot,video_recorder,voice_recorder
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تسجيل وسائط")
        self.القائمة=qt.QListWidget()
        self.القائمة.clicked.connect(self.sh)
        self.القائمة.addItem("تسجيل صوت")
        self.القائمة.addItem("تسجيل فيديو")
        self.القائمة.addItem("إلتقاط صورة")
        self.إظهار=qt.QLabel("الاختصارات")
        self.الاختصارات=qt.QLineEdit()
        self.الاختصارات.setReadOnly(True)
        self.الاختصارات.setAccessibleName("الاختصارات")
        self.الاختصارات.setText("r للتسجيل, p للإيقاف المؤقت, s للإيقاف والحفظ")
        qt1.QShortcut("return",self).activated.connect(self.sh)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.القائمة)
        l.addWidget(self.إظهار)
        l.addWidget(self.الاختصارات)
    def sh(self):
        العناصر=self.القائمة.currentRow()
        if العناصر==0:
            voice_recorder.dialog(self).exec()
        if العناصر==1:
            video_recorder.dialog(self).exec()
        if العناصر==2:
            photo_shoot.dialog(self).exec()