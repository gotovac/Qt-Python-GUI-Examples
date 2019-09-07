import os
import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
        editorFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.editor.setFont(editorFont)
        self.path = None

        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        openFileAction = QAction("Otvori", self)
        saveFileAction = QAction("Spremi", self)
        saveAsFileAction = QAction("Spremi kao...", self)
        openFileAction.triggered.connect(self.open_txt)
        saveFileAction.triggered.connect(self.save_txt)
        saveAsFileAction.triggered.connect(self.saveas_txt)
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction(openFileAction)
        menu.addAction(saveFileAction)
        menu.addAction(saveAsFileAction)
        
        self.show()

    def open_txt(self):
        path, _ = QFileDialog.getOpenFileName(self,
        "Odaberite tekstualnu datoteku",
        "","(*.txt)")

        if path:
            with open(path, 'r') as f:
                text = f.read()
                self.path = path
                self.editor.setPlainText(text)
        else:
            self.path = path
            self.editor.setPlainText(text)

    def save_at_path(self, path):
        text = self.editor.toPlainText()
        if path:
            with open(path, 'w') as f:
                f.write(text)
                self.path = path


    def save_txt(self):
        if self.path is None:
            return self.saveas_txt()

        self.save_at_path(self.path)

    def saveas_txt(self):
        path, _ = QFileDialog.getSaveFileName(self,
        "Spremite tekstualnu datoteku",
        "", "(*.txt)")

        if not path:
            return

        self.save_at_path(path)

    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("TextEditor")
    window = MainWindow()
    window.setGeometry(600,400,600,400)

    app.exec_()