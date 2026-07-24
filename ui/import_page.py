from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QProgressBar,
    QFrame,
    QMessageBox,
)

from core.excel_engine import excel_engine


class ImportPage(QWidget):

    def __init__(self):
        super().__init__()

        self.current_file = None

        self.build_ui()

    ##############################################################

    def build_ui(self):

        main = QVBoxLayout(self)

        main.setSpacing(15)

        ##########################################################
        # Header
        ##########################################################

        title = QLabel("Excel Import")

        title.setStyleSheet("""
        font-size:26px;
        font-weight:bold;
        """)

        main.addWidget(title)

        ##########################################################
        # Toolbar
        ##########################################################

        toolbar = QHBoxLayout()

        self.openButton = QPushButton("Open Excel")

        self.refreshButton = QPushButton("Refresh")

        self.sheetCombo = QComboBox()

        self.sheetCombo.setMinimumWidth(220)

        toolbar.addWidget(self.openButton)

        toolbar.addWidget(self.refreshButton)

        toolbar.addStretch()

        toolbar.addWidget(QLabel("Sheet"))

        toolbar.addWidget(self.sheetCombo)

        main.addLayout(toolbar)

        ##########################################################
        # Upload Area
        ##########################################################

        self.dropFrame = QFrame()

        self.dropFrame.setMinimumHeight(150)

        self.dropFrame.setStyleSheet("""
        QFrame{
            border:2px dashed #3B82F6;
            border-radius:12px;
            background:#F8FAFC;
        }
        """)

        dropLayout = QVBoxLayout(self.dropFrame)

        self.dropLabel = QLabel(
            "Drag & Drop Excel File Here\n\nor\n\nClick 'Open Excel'"
        )

        self.dropLabel.setAlignment(Qt.AlignCenter)

        self.dropLabel.setStyleSheet("""
        font-size:18px;
        color:#555;
        """)

        dropLayout.addStretch()

        dropLayout.addWidget(self.dropLabel)

        dropLayout.addStretch()

        main.addWidget(self.dropFrame)

        ##########################################################
        # Workbook Info
        ##########################################################

        infoLayout = QHBoxLayout()

        self.fileNameLabel = QLabel("Workbook : -")

        self.rowsLabel = QLabel("Rows : 0")

        self.columnsLabel = QLabel("Columns : 0")

        infoLayout.addWidget(self.fileNameLabel)

        infoLayout.addStretch()

        infoLayout.addWidget(self.rowsLabel)

        infoLayout.addWidget(self.columnsLabel)

        main.addLayout(infoLayout)

        ##########################################################
        # Preview Table
        ##########################################################

        self.table = QTableWidget()

        self.table.setAlternatingRowColors(True)

        self.table.setSortingEnabled(False)

        main.addWidget(self.table)

        ##########################################################
        # Progress
        ##########################################################

        self.progress = QProgressBar()

        self.progress.setValue(0)

        main.addWidget(self.progress)

        ##########################################################
        # Signals
        ##########################################################

        self.openButton.clicked.connect(self.open_file)

        self.refreshButton.clicked.connect(self.refresh)

        self.sheetCombo.currentTextChanged.connect(
            self.change_sheet
        )

    ##############################################################

    def open_file(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Excel",
            "",
            "Excel Files (*.xlsx *.xls *.csv)"
        )

        if file_name:
            self.load_file(file_name)

    ##############################################################

    def load_file(self, file_path):
        """
        Implemented in Part 2
        """
        pass

    ##############################################################

    def change_sheet(self):
        """
        Implemented in Part 2
        """
        pass

    ##############################################################

    def refresh(self):

        if self.current_file:
            self.load_file(self.current_file)
