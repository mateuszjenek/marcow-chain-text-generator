from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from controller.QTController import QTController

class QTApplicationWindow(QMainWindow):
    def __init__(self, controller: QTController):
        super(QTApplicationWindow, self).__init__()
        
        self.setWindowTitle("Generator tekstów")

        source_list_widget = QListWidget()
        generated_text_widget = QLabel("")
        
        new_source_action = QAction("&Nowe źródło", self)
        new_source_action.setShortcut(Qt.CTRL + Qt.Key_N)
        new_source_action.triggered.connect(lambda: controller.add_source(source_list_widget, self))

        delete_all_action = QAction("&Usuń wszystkie", self)
        delete_all_action.setShortcut(Qt.CTRL + Qt.Key_U)
        delete_all_action.triggered.connect(lambda: controller.reset_sources(source_list_widget))

        source_option_menu = self.menuBar().addMenu("Źródła &danych")
        source_option_menu.addActions([
            new_source_action,
            delete_all_action
        ])

        main_column = QVBoxLayout()
        main_column.addWidget(QLabel("Źródła danych:"))

        top_row = QHBoxLayout()
        top_row.addWidget(source_list_widget)

        buttons_column = QVBoxLayout()
        new_source_button = QPushButton("Nowe źródło")
        new_source_button.clicked.connect(lambda: controller.add_source(source_list_widget, self))
        buttons_column.addWidget(new_source_button)

        delete_sources_button = QPushButton("Usun wszystkie źródła")
        delete_sources_button.clicked.connect(lambda: controller.reset_sources(source_list_widget))
        buttons_column.addWidget(delete_sources_button)

        generate_button = QPushButton("Generuj")
        generate_button.clicked.connect(lambda: controller.generate_sentence(generated_text_widget))
        buttons_column.addWidget(generate_button)

        top_row.addLayout(buttons_column)
        main_column.addLayout(top_row)

        main_column.addSpacing(10)

        generated_text_box = QGroupBox("Wygenerowany tekst:")
        generated_text_container = QVBoxLayout()
        generated_text_container.addWidget(generated_text_widget)
        generated_text_box.setLayout(generated_text_container)

        main_column.addWidget(generated_text_box)

        widget = QWidget()
        widget.setLayout(main_column)
        self.setCentralWidget(widget)
       
