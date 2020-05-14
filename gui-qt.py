from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from view.qt import ApplicationWindow
from viewmodel.ViewModel import ViewModel

view_model = ViewModel()

app = QApplication([])
window = ApplicationWindow(view_model)
window.show()
app.exec_()