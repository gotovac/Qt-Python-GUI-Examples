# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Thu Sep  5 02:50:17 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 20, 301, 61))
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.btnKreni = QtWidgets.QPushButton(self.centralwidget)
        self.btnKreni.setGeometry(QtCore.QRect(20, 190, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnKreni.setFont(font)
        self.btnKreni.setObjectName("btnKreni")
        self.brojSekundi = QtWidgets.QSpinBox(self.centralwidget)
        self.brojSekundi.setGeometry(QtCore.QRect(20, 120, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.brojSekundi.setFont(font)
        self.brojSekundi.setMinimum(0)
        self.brojSekundi.setMaximum(999)
        self.brojSekundi.setObjectName("brojSekundi")
        self.lblBrojSek = QtWidgets.QLabel(self.centralwidget)
        self.lblBrojSek.setGeometry(QtCore.QRect(20, 100, 301, 16))
        self.lblBrojSek.setObjectName("lblBrojSek")
        self.lblKraj = QtWidgets.QLabel(self.centralwidget)
        self.lblKraj.setGeometry(QtCore.QRect(20, 280, 301, 20))
        self.lblKraj.setTextFormat(QtCore.Qt.RichText)
        self.lblKraj.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKraj.setObjectName("lblKraj")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Countdown", None, -1))
        self.btnKreni.setText(QtWidgets.QApplication.translate("MainWindow", "Kreni!", None, -1))
        self.lblBrojSek.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Broj sekundi</span></p></body></html>", None, -1))
        self.lblKraj.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#fe0101;\"></span></p></body></html>", None, -1))

