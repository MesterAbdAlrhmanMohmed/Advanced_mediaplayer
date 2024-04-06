from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import Audio,Video,Image
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced media player")
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.play)
        self.الخيارات.addItem("تشغيل فيديو")
        self.الخيارات.addItem("تشغيل صوت")
        self.الخيارات.addItem("عرض صورة")
        self.الخيارات.addItem("دليل المستخدم, مهم")
        self.الاختيار=qt.QPushButton("إختيار")
        self.الاختيار.setShortcut("return")
        self.الاختيار.clicked.connect(self.play)
        l=qt.QVBoxLayout()        
        l.addWidget(self.الخيارات)
        l.addWidget(self.الاختيار)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def play(self):
        العناصر=self.الخيارات.currentRow()
        if العناصر ==0:
            Video.dialog(self).exec()
        if العناصر ==1:
            Audio.dialog(self).exec()
        if العناصر ==2:
            Image.dialog(self).exec()
        if العناصر ==3:
            qt.QMessageBox.information(self,"دليل المستخدم","""
1. زر المسافة: تشغيل/إيقاف مؤقت.
2. حرف S: إيقاف.
3. التقديم السريع لمدة 5 ثواني: السهم الأيمن.
4. الترجيع السريع لمدة 5 ثواني: السهم الأيسر.
5. التقديم السريع لمدة 10 ثواني: السهم الأعلى.
6. الترجيع السريع لمدة 10 ثواني: السهم الأسفل.
                                       
لفتح الcombobox في نافذة فتح الفيديوهات عبر الإنترنت نقوم بالضغط على alt زائد سهم.                                       
تحذير, يرجى عدم استخدام هذه الاختصارات عندما يكون المؤشر في مربع الكتابة, يرجى أيضا عدم الخروج من أي نافذة في حالة تشغيل أي مقطع قبل إيقافه أولا.
مع تحياتي, مطور البرنامج عبد الرحمن محمد """)
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()