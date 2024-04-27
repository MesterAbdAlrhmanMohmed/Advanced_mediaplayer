from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import os
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("الصور")
        self.showFullScreen()
        self.فتح = qt.QPushButton("فتح مجلد")
        self.فتح.setDefault(True)        
        self.فتح.clicked.connect(self.opinFile)
        self.التعديل = qt.QLineEdit()
        self.التعديل.setAccessibleName("مسار المجلد")
        self.التعديل.setReadOnly(True)
        self.القائمة = qt.QComboBox()
        self.image = qt.QLabel()
        self.عرض = qt.QPushButton("عرض")
        self.عرض.setDefault(True)
        self.عرض.clicked.connect(self.displayImage)
        layout = qt.QVBoxLayout(self)                            
        layout.addWidget(self.فتح)
        layout.addWidget(self.التعديل)
        layout.addWidget(self.القائمة)
        layout.addWidget(self.image)
        layout.addWidget(self.عرض)
    def opinFile(self):
        folder_path = qt.QFileDialog.getExistingDirectory(self, "فتح مجلد")
        if folder_path:
            self.التعديل.setText(folder_path)  
            self.populateComboBox(folder_path)
    def populateComboBox(self, folder_path):
        self.القائمة.clear()  
        self.القائمة.addItem("محتوا المجلد")        
        audio_formats=['.mp3', '.wav', '.wma', '.aac', '.m4a', '.flac', '.ogg', '.opus', '.ape', '.mpga', '.alac', '.wv', '.mka','.aiff','.au','.dss','.iff','.m4r']
        video_formats=['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.3gp', '.webm', '.rm', '.m2ts', '.vob', '.mts', '.mxf','.SWF','.AV1','.VP9']
        image_formats=['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.ai', '.raw', '.svg', '.heic', '.webp', '.ps','.EPS','.PCT','.TGA','.FITS','.JP2']
        for file_name in os.listdir(folder_path):
            if any(file_name.endswith(format) for format in image_formats):
                self.القائمة.addItem(file_name)

    def displayImage(self):
        selected_image = self.القائمة.currentText()
        folder_path = self.التعديل.text()
        image_path = os.path.join(folder_path, selected_image)
        if os.path.isfile(image_path):
            pixmap = qt1.QPixmap(image_path)
            self.image.setPixmap(pixmap)
        else:
            qt.QMessageBox.warning(self, "تنبيه", "يرجى تحديد صورة صالحة للعرض")