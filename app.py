import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from launcher import Launcher


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Workday Chronometric Professional")
    app.setApplicationVersion("12.0 Enterprise")
    app.setOrganizationName("Vikrant Ambani")

    launcher = Launcher()
    launcher.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
