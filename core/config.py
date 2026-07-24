import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".workday_chronometric"
CONFIG_FILE = CONFIG_DIR / "settings.json"


DEFAULT_SETTINGS = {
    "theme": "dark",
    "accent": "#2563EB",
    "company": "Workday Chronometric",
    "auto_backup": True,
    "backup_days": 30,
    "window_width": 1600,
    "window_height": 900,
    "recent_files": []
}


class Config:

    def __init__(self):
        CONFIG_DIR.mkdir(exist_ok=True)
        self.settings = DEFAULT_SETTINGS.copy()
        self.load()

    def load(self):
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, "r") as f:
                    self.settings.update(json.load(f))
            except Exception:
                pass

    def save(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key):
        return self.settings.get(key)

    def set(self, key, value):
        self.settings[key] = value
        self.save()


config = Config()
