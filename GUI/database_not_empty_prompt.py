from PyQt5.QtWidgets import QVBoxLayout, QDialog, QLabel
from Business_Side.data_repo import DataRepo
from GUI.button_creator import create_button


class DatabaseNotEmptyPrompt(QDialog):
    _datarepo: DataRepo

    def __init__(self, datarepo):
        super().__init__()
        self._datarepo = datarepo
        self.setWindowTitle("Database not empty")
        message = QLabel("The database is not empty, would you like to clear it?")
        layout = QVBoxLayout()
        layout.addWidget(message)
        layout.addWidget(self._clear_database_button())
        layout.addWidget(self._no_button())
        self.setLayout(layout)

    def _clear_database_button(self):
        return create_button("Clear Database", self._clear_database_action)

    def _no_button(self):
        return create_button("No!", self._quit_window_action)

    def _quit_window_action(self):
        self.close()

    def _clear_database_action(self):
        self._datarepo.clear_database()
        self._quit_window_action()
