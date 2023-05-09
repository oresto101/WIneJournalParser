from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from GUI.button_creator import create_button


class AveragePricePrompt(QDialog):
    def __init__(self, avg):
        super().__init__()
        self.setWindowTitle("Average Price")
        message = QLabel(f"The average price is: {avg}")
        layout = QVBoxLayout()
        layout.addWidget(message)
        layout.addWidget(self._okay_button())
        self.setLayout(layout)

    def _okay_button(self):
        return create_button("Thank you, Master!", self._quit_window_action)

    def _quit_window_action(self):
        self.close()