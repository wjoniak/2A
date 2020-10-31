from PyQt5.QtWidgets import QApplication, QWidget


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        self.resize(300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()

def closeEvent(self, event):
    odp = QMessageBox.question(
        self, 'Komunikat',
        "Czy na pewno koniec?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if odp == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()