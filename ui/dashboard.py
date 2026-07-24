from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)

from PySide6.QtGui import QFont

from ui.widgets.kpi_card import KPICard


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Dashboard")

        title.setFont(QFont("Segoe UI", 24, QFont.Bold))

        layout.addWidget(title)

        grid = QGridLayout()

        self.totalEmployees = KPICard(
            "Employees",
            0,
            "#3B82F6"
        )

        self.totalOT = KPICard(
            "Overtime",
            "0 hrs",
            "#10B981"
        )

        self.totalLeave = KPICard(
            "Leave",
            0,
            "#F59E0B"
        )

        self.attendance = KPICard(
            "Attendance",
            "0%",
            "#EF4444"
        )

        grid.addWidget(self.totalEmployees, 0, 0)
        grid.addWidget(self.totalOT, 0, 1)
        grid.addWidget(self.totalLeave, 1, 0)
        grid.addWidget(self.attendance, 1, 1)

        layout.addLayout(grid)

        layout.addStretch()

    def refresh(self):

        print("Dashboard Refreshed")
