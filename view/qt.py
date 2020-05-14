from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from viewmodel.ViewModel import ViewModel

class ApplicationWindow(QMainWindow):
    def __init__(self, view_model: ViewModel):
        super(ApplicationWindow, self).__init__()
        
        self.view_model = view_model
        self.setWindowTitle("Generator tekstów")
        
        new_source_action = QAction("&Nowe źródło", self)
        new_source_action.setShortcut(Qt.CTRL + Qt.Key_N)
        # TODO: Show widget to search files ad trigger func add_source
        #an.triggered.connect( self.addNewSource )\
        new_source_action.triggered.connect(self.__get_file_dialog)

        delete_all_action = QAction( "&Usuń wszystkie",self )
        delete_all_action.setShortcut(Qt.CTRL + Qt.Key_U)
        delete_all_action.triggered.connect(self.view_model.reset_sources)

        source_option_menu = self.menuBar().addMenu( "Źródła &danych" )
        source_option_menu.addActions([
            new_source_action,
            delete_all_action
        ])

        information_action = QAction( "&Informacje",self )
        information_action.setShortcut(Qt.CTRL + Qt.Key_I)
        # TODO: Show widget about
        #ai.triggered.connect( self.showAboutWindow )
        about_oprion_menu = self.menuBar().addMenu( "&O programie" )
        about_oprion_menu.addAction(information_action)

        main_column = QVBoxLayout()
        main_column.addWidget(QLabel( "Źródła danych:" ))

        top_row = QHBoxLayout()
        source_list_widget = QListWidget()
        top_row.addWidget(source_list_widget)

        column2 = QVBoxLayout()
        new_source_button = QPushButton( "Nowe źródło")
        column2.addWidget(new_source_button)
        delete_sources_button = QPushButton( "Usun wszystkie źródła")
        column2.addWidget(delete_sources_button)
        generate_button = QPushButton( "Generuj" )
        column2.addWidget(generate_button)

        top_row.addLayout(column2)
        main_column.addLayout(top_row)

        main_column.addSpacing(10)

        box = QGroupBox("Wygenerowany tekst:")
        column3 = QVBoxLayout()
        column3.addWidget(QLabel("Twój tato musi być tak przystojnym..."))
        box.setLayout(column3)

        main_column.addWidget(box)

        widget = QWidget()
        widget.setLayout(main_column)

        self.setCentralWidget(widget)

    def __get_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            return dialog.selectFile()
        return ""
