from core.config import config


DARK = """
QMainWindow{
    background:#111827;
}

QWidget{
    background:#111827;
    color:white;
}

QStatusBar{
    background:#1F2937;
    color:white;
}

QToolBar{
    background:#1F2937;
    spacing:8px;
}

QPushButton{
    background:#2563EB;
    border:none;
    border-radius:8px;
    padding:8px;
    color:white;
}

QPushButton:hover{
    background:#3B82F6;
}
"""

LIGHT = """
QMainWindow{
    background:white;
}

QWidget{
    background:white;
    color:#111;
}

QStatusBar{
    background:#ECECEC;
}

QToolBar{
    background:#F5F5F5;
}

QPushButton{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:8px;
    padding:8px;
}

QPushButton:hover{
    background:#3B82F6;
}
"""


def load_theme():
    if config.get("theme") == "dark":
        return DARK

    return LIGHT
