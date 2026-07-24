from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt


class KPICard(QFrame):

    def __init__(self, title, value, color="#2563EB"):
        super().__init__()

        self.title = QLabel(title)
        self.value = QLabel(str(value))

        self.build_ui(color)

    def build_ui(self, color):

        self.setMinimumHeight(140)
        self.setMaximumHeight(140)

        self.setStyleSheet(f"""
        QFrame{{
            background:#1E293B;
            border-radius:18px;
            border:2px solid {color};
        }}

        QLabel{{
            color:white;
            background:transparent;
        }}
        """)

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 120))
        shadow.setOffset(0, 8)

        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self)

        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Segoe UI", 11))

        self.value.setAlignment(Qt.AlignCenter)
        self.value.setFont(QFont("Segoe UI", 28, QFont.Bold))

        layout.addStretch()
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        layout.addStretch()

    def update_value(self, value):
        self.value.setText(str(value))
