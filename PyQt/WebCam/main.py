import os
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.path = None
        self.cameraList = QCameraInfo.availableCameras()

        self.cameraView = QCameraViewfinder()
        self.cameraView.show()
        self.setCentralWidget(self.cameraView)

        self.camera = QCamera(self.cameraList[0])
        self.camera.setViewfinder(self.cameraView)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.identity = 0

        toolbar = QToolBar("WebCam")
        self.addToolBar(toolbar)
        takePhotoAction = QAction("Slikaj", self)
        changePathAction = QAction("Promijeni lokaciju", self)
        takePhotoAction.triggered.connect(self.take_photo)
        changePathAction.triggered.connect(self.change_path)
        toolbar.addAction(takePhotoAction)
        toolbar.addAction(changePathAction)

        self.show()

    def take_photo(self):
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        if self.path:
            self.capture.capture(os.path.join(self.path,
            "%04d-%s.jpg" % (self.identity, timestamp)))
            self.identity += 1
        

    def change_path(self):
        path = QFileDialog.getExistingDirectory(self, "Odaberi novu lokaciju", "")
        if path:
            self.path = path
            self.identity = 0

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("WebCam")

    window = MainWindow()
    app.exec_()