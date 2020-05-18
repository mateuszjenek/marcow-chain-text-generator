from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from view.QTApplicationWindow import QTApplicationWindow
from controller.QTController import QTController

controller = QTController()

app = QApplication([])
window = QTApplicationWindow(controller)
window.show()
app.exec_()