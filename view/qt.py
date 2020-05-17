from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from controller.QTController import QTController

class ApplicationWindow(QMainWindow):
    def __init__(self, controller: QTController):
        super(ApplicationWindow, self).__init__()
        
        self.controller = controller
        self.setWindowTitle("Generator tekstów")

        source_list_widget = QListWidget()
        generated_text_widget = QLabel("Twój tato musi być tak przystojnym...")
        
        new_source_action = QAction("&Nowe źródło", self)
        new_source_action.setShortcut(Qt.CTRL + Qt.Key_N)
        new_source_action.triggered.connect(lambda: self.controller.add_source(source_list_widget, self))

        delete_all_action = QAction("&Usuń wszystkie", self)
        delete_all_action.setShortcut(Qt.CTRL + Qt.Key_U)
        delete_all_action.triggered.connect(lambda: self.controller.reset_sources(source_list_widget))

        source_option_menu = self.menuBar().addMenu("Źródła &danych")
        source_option_menu.addActions([
            new_source_action,
            delete_all_action
        ])

        information_action = QAction("&Informacje", self)
        information_action.setShortcut(Qt.CTRL + Qt.Key_I)
        # TODO: Show widget about
        #ai.triggered.connect( self.showAboutWindow )
        about_option_menu = self.menuBar().addMenu("&O programie")
        about_option_menu.addAction(information_action)

        main_column = QVBoxLayout()
        main_column.addWidget(QLabel("Źródła danych:"))

        top_row = QHBoxLayout()
        top_row.addWidget(source_list_widget)

        buttons_column = QVBoxLayout()
        new_source_button = QPushButton("Nowe źródło")
        new_source_button.clicked.connect(lambda: self.controller.add_source(source_list_widget, self))
        buttons_column.addWidget(new_source_button)

        delete_sources_button = QPushButton("Usun wszystkie źródła")
        delete_sources_button.clicked.connect(lambda: self.controller.reset_sources(source_list_widget))
        buttons_column.addWidget(delete_sources_button)

        generate_button = QPushButton("Generuj")
        generate_button.clicked.connect(lambda: self.controller.generate_sentence(generated_text_widget))
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
       
