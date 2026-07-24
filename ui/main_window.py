from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QStackedWidget,
    QStatusBar,
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Workday Chronometric Professional")

        self.resize(1600, 900)

        self.setup_ui()

    def setup_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        mainLayout = QHBoxLayout()

        mainLayout.setContentsMargins(0, 0, 0, 0)

        central.setLayout(mainLayout)

        #################################################

        self.sidebar = Sidebar()

        #################################################

        self.pages = QStackedWidget()

        #################################################

        self.dashboard = Dashboard()

        self.pages.addWidget(self.dashboard)

        #################################################

        mainLayout.addWidget(self.sidebar)

        mainLayout.addWidget(self.pages)

        #################################################

        self.sidebar.dashboardButton.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.dashboard)
        )

        #################################################

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

        #################################################

        toolbar = self.addToolBar("Main")

        refresh = QAction("Refresh", self)

        refresh.triggered.connect(self.refresh)

        toolbar.addAction(refresh)

    def refresh(self):

        self.dashboard.refresh()
