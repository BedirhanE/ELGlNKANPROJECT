from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from arayuz import Ui_MainWindow #arayüzü mainin içerisine gömmek için import etmem gerekiyor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PushButton'a tıklama olayını bağlayan işlevi tanımla
        self.ui.pushButton.clicked.connect(self.calculate_sum)
        #self.ui.lineEdit_2.returnPressed.connect(self.calculate_sum)
        

    def calculate_sum(self):
        sayi1 = int(self.ui.lineEdit.text())  # İlk sayıyı al
        sayi2 = int(self.ui.lineEdit_2.text())  # İkinci sayıyı al
        sonuc = sayi1 + sayi2  # Sayıları topla
        self.ui.lineEdit_3.setText(str(sonuc))  # Sonucu QLineEdit'e yazdır


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  
    window = MainWindow()# Ana pencereyi oluştur ve gösterir.
    window.show()
    sys.exit(app.exec())
