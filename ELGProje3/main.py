from PyQt6.QtWidgets import QApplication, QMainWindow
from arayuz import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.radioButton.clicked.connect(self.update_label)
        self.radioButton_2.clicked.connect(self.update_label)
        self.radioButton_3.clicked.connect(self.update_label)
        self.radioButton_4.clicked.connect(self.update_label)
        self.pushButton.clicked.connect(self.show_result)

    def update_label(self):
        if self.radioButton.isChecked():
            self.label.setText("İlköğretim seçildi.")
        elif self.radioButton_2.isChecked():
            self.label.setText("Lise seçildi.")
        elif self.radioButton_3.isChecked():
            self.label.setText("Üniversite seçildi.")
        elif self.radioButton_4.isChecked():
            self.label.setText("Diğer seçildi.")

    def show_result(self):
        if self.radioButton.isChecked():
            self.label.setText("İlköğretim seçildi.")
        elif self.radioButton_2.isChecked():
            self.label.setText("Lise seçildi.")
        elif self.radioButton_3.isChecked():
            self.label.setText("Üniversite seçildi.")
        elif self.radioButton_4.isChecked():
            self.label.setText("Diğer seçildi.")
        else:
            self.label.setText("Hiçbir seçenek seçilmedi.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
