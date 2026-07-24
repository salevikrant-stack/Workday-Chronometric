from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):
        main = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))

        main.addWidget(title)

        cards = QHBoxLayout()

        cards.addWidget(self.create_card("Employees", "0"))
        cards.addWidget(self.create_card("Overtime", "0 Hrs"))
        cards.addWidget(self.create_card("Leave", "0"))
        cards.addWidget(self.create_card("Attendance", "0%"))

        main.addLayout(cards)

        welcome = QLabel(
            "Welcome to Workday Chronometric Professional\n\n"
            "This dashboard will display analytics, charts, KPIs,\n"
            "attendance trends, overtime summaries, and reports."
        )

        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("font-size:16px;")

        main.addStretch()
        main.addWidget(welcome)
        main.addStretch()

    def create_card(self, title, value):
        frame = QFrame()

        frame.setMinimumHeight(120)

        frame.setStyleSheet("""
        QFrame{
            background:white;
            border:1px solid #dcdcdc;
            border-radius:12px;
        }
        """)

        layout = QVBoxLayout(frame)

        lblTitle = QLabel(title)
        lblTitle.setAlignment(Qt.AlignCenter)
        lblTitle.setFont(QFont("Segoe UI", 11))

        lblValue = QLabel(value)
        lblValue.setAlignment(Qt.AlignCenter)
        lblValue.setFont(QFont("Segoe UI", 24, QFont.Bold))

        layout.addStretch()
        layout.addWidget(lblTitle)
        layout.addWidget(lblValue)
        layout.addStretch()

        return frame

    def refresh(self):
        print("Dashboard refreshed.")
