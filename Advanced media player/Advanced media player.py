from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import Audio,Video,Image,folder,about,player,sys,media,photo_player
class main (qt.QMainWindow):
    def __init__(self):        
        super().__init__()                                                
        self.setWindowTitle("Advanced media player")
        audio_formats = [".mp3", ".wav", ".wma", ".aac", ".m4a", ".flac", ".ogg", ".opus", ".ape", ".mpga", ".alac", ".wv", ".mka", ".aiff", ".au", ".dss", ".iff", ".m4r", ".m4b", ".midi", ".mid", ".ac3", ".tta", ".m3u"]
        video_formats = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".3gp", ".webm", ".rm", ".m2ts", ".vob", ".mts", ".mxf", ".SWF", ".AV1", ".VP9", ".MPG", ".M4V", ".WMV", ".ASF", ".mpeg", ".ogv", ".rmvb", ".divx", ".m2v"]
        image_formats = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".psd", ".ai", ".raw", ".svg", ".heic", ".webp", ".ps", ".EPS", ".PCT", ".TGA", ".FITS", ".JP2", ".EXR", ".PBM", ".ico", ".tif", ".tga", ".pcx", ".jif", ".hdr", ".dng", ".jxr", ".dib"]
        formate=audio_formats+video_formats
        if len(sys.argv) > 1:            
            مسار=" ".join(sys.argv[1:])
            for format in formate:
                if مسار.endswith(format):
                    player.player(self, " ".join(sys.argv[1:])).exec()
                    break
            for formatt in image_formats:
                if مسار.endswith(formatt):
                    photo_player.photo_player(self, " ".join(sys.argv[1:])).exec()
                    break        
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.play)        
        self.الخيارات.addItem("فتح مجلد")
        self.الخيارات.addItem("تشغيل فيديو")
        self.الخيارات.addItem("تشغيل صوت")
        self.الخيارات.addItem("عرض صورة")
        self.الخيارات.addItem("تسجيل وسائط")
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
        if العناصر==4:
            media.dialog(self)            .exec()
        if العناصر ==5:
            qt.QMessageBox.information(self,"دليل المستخدم","""1. زر المسافة: تشغيل/إيقاف مؤقت.
2. حرف S: إيقاف.
3. التقديم السريع لمدة 5 ثواني: السهم الأيمن.
4. الترجيع السريع لمدة 5 ثواني: السهم الأيسر.
5. التقديم السريع لمدة 10 ثواني: السهم الأعلى.
6. الترجيع السريع لمدة 10 ثواني: السهم الأسفل.
7. التقديم السريع لمدة 30 ثانية: CTRL+السهم الأيمن.
8. الترجيع السريع لمدة 30 ثانية: CTRL+السهم الأيسر.
9. التقديم السريع لمدة دقيقة: CTRL+السهم الأعلا.
10. الترجيع السريع لمدة دقيقة: CTRL+السهم الأسفل.
11. اختصارات Ctrl + الرقم" للانتقال مباشرة إلى نسبة محددة من الملف، على سبيل المثال، "Ctrl + 1" للانتقال إلى 10% من الملف، "Ctrl + 2" للانتقال إلى 20%، وهكذا.
12. رفع الصوت: shift+ السهم الأعلى.
13. خفض الصوت: shift+ السهم الأسفل.
في نافذة فتح مجلد فقط,
14. المقطع التالي, shift+ السهم الأيمن.
15. المقطع السابق, shift+ السهم الأيسر.

ملاحظة, في نافذة فتح مجلد, للإيقاف المؤقت نضغط مسافة وللإستئناف نضغط حرف R.
                                       
لفتح الcombobox نقوم بالضغط على alt زائد سهم لأسفل.
لتفعيل البرنامج في قائمة الفتح باستخدام, نقوم باختيار ملف البرنامج من الجهاز وبعدها نقوم بتحديد مربع الاختيار الخاص بجعل المشغل كافتراضي.
تحذير, يرجى عدم استخدام هذه الاختصارات عندما يكون المؤشر في مربع الكتابة, يرجى أيضا عدم الخروج من أي نافذة في حالة تشغيل أي مقطع قبل إيقافه أولا.
مع تحياتي, مطور البرنامج عبد الرحمن محمد""")
        if العناصر==6:
          about.dialog(self)      .exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()