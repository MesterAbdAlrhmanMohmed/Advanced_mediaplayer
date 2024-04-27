from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import Audio,Video,Image,folder,about
class main (qt.QMainWindow):
    def __init__(self):        
        super().__init__()                        
        self.setWindowTitle("Advanced media player")
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.play)        
        self.الخيارات.addItem("فتح مجلد")
        self.الخيارات.addItem("تشغيل فيديو")
        self.الخيارات.addItem("تشغيل صوت")
        self.الخيارات.addItem("عرض صورة")
        self.الخيارات.addItem("دليل المستخدم, مهم")
        self.الخيارات.addItem("عن المطور")
        qt1.QShortcut("return",self).activated.connect(self.play)
        l=qt.QVBoxLayout()        
        l.addWidget(self.الخيارات)        
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def play(self):
        العناصر=self.الخيارات.currentRow()
        if العناصر ==0:
            folder.dialog(self).exec()
        if العناصر ==1:
            Video.dialog(self).exec()
        if العناصر ==2:
            Audio.dialog(self).exec()
        if العناصر ==3:
            Image.dialog(self).exec()
        if العناصر ==4:
            qt.QMessageBox.information(self,"دليل المستخدم","""
1. زر المسافة: تشغيل/إيقاف مؤقت.
2. حرف S: إيقاف.
3. التقديم السريع لمدة 5 ثواني: السهم الأيمن.
4. الترجيع السريع لمدة 5 ثواني: السهم الأيسر.
5. التقديم السريع لمدة 10 ثواني: السهم الأعلى.
6. الترجيع السريع لمدة 10 ثواني: السهم الأسفل.
7. التقديم السريع لمدة 30 ثانية: CTRL+السهم الأيمن.
8. الترجيع السريع لمدة 30 ثانية: CTRL+السهم الأيسر.                                       
9. التقديم السريع لمدة دقيقة: CTRL+السهم الأعلا.                                       
10. الترجيع السريع لمدة دقيقة: CTRL+السهم الأسفل.                                       
                                       
11. اختصارات "Ctrl + الرقم" للانتقال مباشرة إلى نسبة محددة من الملف، على سبيل المثال، "Ctrl + 1" للانتقال إلى 10% من الملف، "Ctrl + 2" للانتقال إلى 20%، وهكذا.
ملاحظة, في نافذة فتح مجلد, للإيقاف المؤقت نضغط مسافة وللإستئناف نضغط حرف R.                                                                              
                                       
لفتح الcombobox نقوم بالضغط على alt زائد سهم لأسفل.                                       
تحذير, يرجى عدم استخدام هذه الاختصارات عندما يكون المؤشر في مربع الكتابة, يرجى أيضا عدم الخروج من أي نافذة في حالة تشغيل أي مقطع قبل إيقافه أولا.
مع تحياتي, مطور البرنامج عبد الرحمن محمد """)
        if العناصر==5:
          about.dialog(self)      .exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()