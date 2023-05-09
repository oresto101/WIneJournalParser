from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from GUI.button_creator import create_button


class CriteriaNotSetPrompt(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criteria not set")
        message = QLabel("Please select at least 2 criteria")
        layout = QVBoxLayout()
        layout.addWidget(message)
        layout.addWidget(self._okay_button())
        self.setLayout(layout)

    def _okay_button(self):
        return create_button("Okay, Master!", self._quit_window_action)

    def _quit_window_action(self):
        self.close()
