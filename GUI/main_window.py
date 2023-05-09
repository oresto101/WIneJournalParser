from PyQt5.QtWidgets import QVBoxLayout, QWidget
from Business_Side.file_operations import delete_file, get_dict_from_json
from Business_Side.data_repo import DataRepo
from GUI.database_not_empty_prompt import DatabaseNotEmptyPrompt
from GUI.set_criteria_prompt import SetCriteriaPrompt
from GUI.data_table import WineEntries
from GUI.button_creator import create_button
from GUI.database_not_existing_prompt import DatabaseNotExistingPrompt


class MainWindow(QWidget):
    _datarepo: DataRepo

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Main Window')
        self._datarepo = DataRepo('data.sqlite')
        self._create_main_window_widgets()

    def _create_main_window_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self._clear_database_button())
        layout.addWidget(self._get_data_button())
        layout.addWidget(self._set_criteria_button())
        layout.addWidget(self._show_database_button())
        layout.addWidget(self._quit_button())
        self.setLayout(layout)

    def _quit_app_action(self):
        delete_file('data.sqlite')
        delete_file('plot.png')
        delete_file('criteria.json')
        self._datarepo.connection.close()
        self.close()

    def _clear_database_action(self):
        self._datarepo.clear_database()

    def _save_data(self, criteria={'points', 'title'}):
        self._datarepo.insert_data(get_dict_from_json('data.json'), get_dict_from_json('criteria.json')['criteria'])

    def _get_data_action(self):
        self._datarepo.create_database()
        if not self._datarepo.is_database_empty():
            self._database_not_empty_window()
            self._datarepo.create_database()
        self._save_data()

    def _quit_button(self):
        return create_button("Quit Application", self._quit_app_action)

    def _get_data_button(self):
        return create_button("Get Data", self._get_data_action)

    def _clear_database_button(self):
        return create_button("Clear Database", self._clear_database_action)

    def _set_criteria_button(self):
        return create_button("Set Download Criteria", self._set_criteria_action)

    def _show_database_button(self):
        return create_button("Show Database", self._show_database_action)

    def _database_not_empty_window(self):
        DatabaseNotEmptyPrompt(self._datarepo).exec()

    def _set_criteria_action(self):
        SetCriteriaPrompt(get_dict_from_json('data.json')[0].keys()).exec()

    def _show_database_action(self):
        if not self._datarepo.table_exists():
            DatabaseNotExistingPrompt().exec()
        else:
            WineEntries(self._datarepo, self).show()
