import sys
import time
from threading import Thread
from PySide2.QtWidgets import QApplication, QMainWindow, QLCDNumber
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pokreni)
        self.countdown = self.ui.lcdNumber

    def pokreni(self):
        t = Thread(target=self._countdown)
        t.start()

    def _countdown(self):
        for i in range(10,-1,-1):
            time.sleep(1)
            self.countdown.display(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())