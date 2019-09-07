import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from ui_locator import *

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnPrikazi.clicked.connect(self.prikazi)
        self.show()

    def prikazi(self):
        lng = self.ui.editLongituda.text()
        lat = self.ui.editLatituda.text()
        url="https://www.google.com/maps/@"+lng+","+lat+",9z"
        self.ui.widget.load(QUrl(url))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("CoordLocator")
    w.show()
    sys.exit(app.exec_())