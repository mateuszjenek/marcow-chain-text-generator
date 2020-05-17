from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from model.MarcowChainFactory import MarcowChainFactory
from model.IMarcowChain import IMarcowChain

class QTController():
    marcow_factory = MarcowChainFactory()

    def __init__(self):
        self.__generator = self.marcow_factory.first_order()
    
    def add_source(self, source_list_widget: QListWidget, parent: QWidget):
        dialog = QFileDialog(parent)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            for file_path in dialog.selectedFiles():
                lines = open(file_path, encoding='utf8').read().splitlines()
                self.__generator.feed(lines)
                source_list_widget.addItem(file_path)

    def reset_sources(self, source_list_widget: QListWidget):
        source_list_widget.clear()
        self.__generator.reset()

    def generate_sentence(self, generated_text_widget: QLabel) -> str:
        generated_text_widget.setText(self.__generator.generate())
        