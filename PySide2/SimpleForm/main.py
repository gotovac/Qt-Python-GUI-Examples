import sys
from PySide2.QtWidgets import QLineEdit, QPushButton, QApplication, QFormLayout, QDialog, QWidget, QLabel

class Form(QFormLayout):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.unosImena = QLineEdit()
        self.unosPrezimena = QLineEdit()
        self.btnPosalji = QPushButton("Pošalji")
        self.lblIspis = QLabel()
        self.addRow("Ime: ", self.unosImena)
        self.addRow("Prezime: ", self.unosPrezimena)
        self.addWidget(self.btnPosalji)
        self.addWidget(self.lblIspis)
        
        self.btnPosalji.clicked.connect(self.ispis)

    def ispis(self):
        self.lblIspis.setText("Ime: " + self.unosImena.text() +
        "\nPrezime: " + self.unosPrezimena.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(300,300,400,175)
    form = Form()
    window.setLayout(form)
    window.setWindowTitle("Jednostavna forma")
    window.show()
    sys.exit(app.exec_())