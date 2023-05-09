from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QDialog, QLabel, QCheckBox
from GUI.criteria_not_set_prompt import CriteriaNotSetPrompt
from GUI.button_creator import create_button
from Business_Side.file_operations import create_json_from_list


class SetCriteriaPrompt(QDialog):
    _all_criteria: dict

    def __init__(self, all_criteria):
        super().__init__()
        self._all_criteria = all_criteria
        self.setWindowTitle("Setting The Criteria")
        message = QLabel("Please set the attributes you would like to see")
        layout = QVBoxLayout()
        checkbox_sublayout = QGridLayout()
        layout.addWidget(message)
        self._checkboxes, positions = self._criteria_checkbox_buttons()
        for position, checkbox in zip(positions, self._checkboxes):
           checkbox_sublayout.addWidget(checkbox, *position)
        layout.addLayout(checkbox_sublayout)
        layout.addWidget(self._save_criteria_button())
        layout.addWidget(self._no_button())
        self.setLayout(layout)

    def _criteria_checkbox_buttons(self):
        checkboxes = []
        positions = []
        for index, criteria in enumerate(self._all_criteria):
            checkbox = QCheckBox(criteria)
            checkboxes.append(checkbox)
            positions.append((int(index / 2) + 1, index % 2))
        return checkboxes, positions

    def _get_criteria(self):
        criteria = set()
        for checkbox in self._checkboxes:
            if checkbox.isChecked():
                criteria.add(checkbox.text())
        return criteria

    def _save_criteria_button(self):
        return create_button("Save Criteria", self._save_criteria_action)

    def _no_button(self):
        return create_button("No!", self._quit_window_action)

    def _quit_window_action(self):
        self.close()

    def _save_criteria_action(self):
        criteria = self._get_criteria()
        if len(criteria) < 2:
            CriteriaNotSetPrompt().exec()
        else:
            create_json_from_list(list(criteria), 'criteria.json')
            self._quit_window_action()
