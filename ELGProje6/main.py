from PyQt6 import QtWidgets
from arayuz import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.currentIndexChanged.connect(self.updateDistricts)  # İl seçimi değiştiğinde ilçeleri güncelle

        self.show()

    def updateDistricts(self):
        city = self.ui.comboBox.currentText()
        self.ui.comboBox_2.clear()

        if city == "İzmir":
            self.ui.comboBox_2.addItem("Karşıyaka")
            self.ui.comboBox_2.addItem("Konak")
            self.ui.comboBox_2.addItem("Bornova")
            # İzmir'in diğer ilçelerini buraya ekleyin
        elif city == "Aydın":
            self.ui.comboBox_2.addItem("Efeler")
            self.ui.comboBox_2.addItem("Nazilli")
            self.ui.comboBox_2.addItem("Söke")
            # Aydın'ın diğer ilçelerini buraya ekleyin
        elif city == "Erzurum":
            self.ui.comboBox_2.addItem("Yakutiye")
            self.ui.comboBox_2.addItem("Palandöken")
            self.ui.comboBox_2.addItem("Aziziye")
            # Erzurum'un diğer ilçelerini buraya ekleyin
        elif city == "Trabzon":
            self.ui.comboBox_2.addItem("Ortahisar")
            self.ui.comboBox_2.addItem("Akçaabat")
            self.ui.comboBox_2.addItem("Yomra")
            # Trabzon'un diğer ilçelerini buraya ekleyin


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
