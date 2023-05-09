from PyQt5.QtWidgets import QPushButton


def create_button(title, action):
    button = QPushButton(title)
    button.clicked.connect(lambda: action())
    return button
