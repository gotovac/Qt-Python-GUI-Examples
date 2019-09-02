import sys
import random
from PySide2.QtWidgets import QApplication, QPushButton, QLabel, QMessageBox, QWidget
from PySide2.QtCore import Slot

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 250)
button = QPushButton(window)
button.setText("Izvuci dobitni broj između 1 i 100")
button.setGeometry(100,100,200,50)

@Slot()
def izvuci_broj():
    msg = QMessageBox()
    msg.setText("Dobitni broj je: " + str(random.randint(1,101)))
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

button.clicked.connect(izvuci_broj)
window.show()

app.exec_()

