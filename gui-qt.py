from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from view.qt import ApplicationWindow
from controller.QTController import QTController

controller = QTController()

app = QApplication([])
window = ApplicationWindow(controller)
window.show()
app.exec_()