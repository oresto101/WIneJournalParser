from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from GUI.button_creator import create_button


class CountryPieChartPrompt(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Country Pie Chart")
        message = QLabel("Countries producing the most wine")
        layout = QVBoxLayout()
        layout.addWidget(message)
        picture = QLabel()
        picture.setPixmap(QPixmap('plot.png'))
        layout.addWidget(picture)
        layout.addWidget(self._okay_button())
        self.setLayout(layout)

    def _okay_button(self):
        return create_button("Thank you, Master!", self._quit_window_action)

    def _quit_window_action(self):
        self.close()