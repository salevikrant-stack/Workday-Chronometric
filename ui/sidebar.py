from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy,
    QFrame,
)


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(250)
        self.setObjectName("Sidebar")

        self.build_ui()
        self.apply_style()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(12)

        title = QLabel("Workday\nChronometric")
        title.setAlignment(Qt.AlignCenter)

        font = QFont("Segoe UI", 16)
        font.setBold(True)
        title.setFont(font)

        layout.addWidget(title)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout.addWidget(line)

        self.dashboardButton = QPushButton("🏠 Dashboard")
        self.importButton = QPushButton("📂 Import")
        self.timesheetButton = QPushButton("📋 Timesheets")
        self.overtimeButton = QPushButton("⏰ Overtime")
        self.leaveButton = QPushButton("🌴 Leave")
        self.analyticsButton = QPushButton("📊 Analytics")
        self.reportsButton = QPushButton("📈 Reports")
        self.aiButton = QPushButton("🤖 AI Assistant")
        self.settingsButton = QPushButton("⚙ Settings")

        buttons = [
            self.dashboardButton,
            self.importButton,
            self.timesheetButton,
            self.overtimeButton,
            self.leaveButton,
            self.analyticsButton,
            self.reportsButton,
            self.aiButton,
            self.settingsButton,
        ]

        for button in buttons:
            button.setMinimumHeight(42)
            button.setCursor(Qt.PointingHandCursor)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            layout.addWidget(button)

        layout.addStretch()

        version = QLabel("Version 12 Enterprise")
        version.setAlignment(Qt.AlignCenter)
        layout.addWidget(version)

    def apply_style(self):
        self.setStyleSheet("""
        QWidget#Sidebar{
            background:#1F2937;
        }

        QLabel{
            color:white;
        }

        QPushButton{
            background:#374151;
            color:white;
            border:none;
            border-radius:8px;
            padding:10px;
            text-align:left;
            font-size:13px;
        }

        QPushButton:hover{
            background:#2563EB;
        }

        QPushButton:pressed{
            background:#1D4ED8;
        }

        QFrame{
            color:#555;
        }
        """)
