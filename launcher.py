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
from core.logger import logger


class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.info("Launcher Started")

        self.setWindowTitle("Workday Chronometric Professional")
        self.resize(900, 500)
        self.setMinimumSize(900, 500)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(15)

        # ==========================================
        # Logo / Title
        # ==========================================

        title = QLabel("Workday Chronometric Professional")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))

        subtitle = QLabel("Enterprise Edition v12")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 12))

        description = QLabel(
            "Professional Workday Analytics, Reporting, and Productivity Suite"
        )
        description.setAlignment(Qt.AlignCenter)
        description.setWordWrap(True)

        # ==========================================
        # Launch Button
        # ==========================================

        start = QPushButton("🚀 Launch Application")
        start.setFixedWidth(260)
        start.setFixedHeight(50)
        start.clicked.connect(self.launch)

        # ==========================================
        # Footer
        # ==========================================

        footer = QLabel(
            "© 2026 Workday Chronometric Professional\nDeveloped by Vikrant Ambani"
        )
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: gray;")

        # ==========================================
        # Add Widgets
        # ==========================================

        layout.addStretch()

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(description)

        layout.addSpacing(25)

        layout.addWidget(start, alignment=Qt.AlignCenter)

        layout.addStretch()

        layout.addWidget(footer)

    def launch(self):
        logger.info("Opening Main Window")

        self.window = MainWindow()
        self.window.show()

        self.close()
