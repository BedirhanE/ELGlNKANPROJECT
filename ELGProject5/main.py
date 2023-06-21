from PyQt6.QtWidgets import QApplication, QMainWindow
from arayuz import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.show_result)

    def show_result(self):
        result = ""
        checkboxes = self.groupBox.findChildren(QCheckBox)
        for checkbox in checkboxes:
            if checkbox.isChecked():
                result += checkbox.text() + " "
        self.label.setText(result.strip())


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QCheckBox
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
