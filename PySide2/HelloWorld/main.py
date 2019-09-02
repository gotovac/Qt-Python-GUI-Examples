import sys                                                                           
from PySide2 import QtCore, QtWidgets                                           
                                                                                                                                              
app = QtWidgets.QApplication(sys.argv)                                               
                                                                                                                                                       
mywindow = QtWidgets.QWidget()                                                       
mywindow.resize(500, 300)                                                                                                                               
mylabel = QtWidgets.QLabel(mywindow)                                                    
mylabel.setText('Hello World!')                                                                                        
mywindow.show()                                                                         
                                                                                                                                               
sys.exit(app.exec_())