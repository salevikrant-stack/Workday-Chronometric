from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ui.main_window import MainWindow


class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Workday Chronometric Professional")

        self.resize(900, 500)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Workday Chronometric Professional")

        title.setFont(QFont("Segoe UI", 24, QFont.Bold))

        subtitle = QLabel("Enterprise Edition v12")

        subtitle.setFont(QFont("Segoe UI", 12))

        start = QPushButton("Launch Application")

        start.setFixedHeight(45)

        start.clicked.connect(self.launch)

        layout.addWidget(title)

        layout.addWidget(subtitle)

        layout.addSpacing(20)

        layout.addWidget(start)

    def launch(self):
        self.window = MainWindow()
        self.window.show()
        self.close()
