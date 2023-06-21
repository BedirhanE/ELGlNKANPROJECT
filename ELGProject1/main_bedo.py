from PyQt6 import QtCore, QtGui, QtWidgets
from bedo1 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changeFont)

    def changeFont(self):
        font = QtGui.QFont(self.ui.fontComboBox.currentFont())
        font.setPointSize(self.ui.spinBox.value())
        self.ui.textEdit.setFont(font)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
