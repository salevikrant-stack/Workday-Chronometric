from pathlib import Path
import pandas as pd


class FileValidator:
    """
    Validates files before importing.

    Supported:
        • .xlsx
        • .xls
        • .csv
    """

    SUPPORTED_EXTENSIONS = {
        ".xlsx",
        ".xls",
        ".csv"
    }

    MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB

    def validate(self, file_path):

        path = Path(file_path)

        # -----------------------------
        # File Exists
        # -----------------------------
        if not path.exists():
            return False, "File does not exist."

        # -----------------------------
        # Extension
        # -----------------------------
        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            return (
                False,
                f"Unsupported file type: {path.suffix}"
            )

        # -----------------------------
        # File Size
        # -----------------------------
        size = path.stat().st_size

        if size == 0:
            return False, "The selected file is empty."

        if size > self.MAX_FILE_SIZE:
            return (
                False,
                "File exceeds 100 MB limit."
            )

        # -----------------------------
        # Try opening file
        # -----------------------------
        try:

            if path.suffix.lower() == ".csv":
                pd.read_csv(path, nrows=5)

            else:
                pd.ExcelFile(path)

        except Exception as e:

            return (
                False,
                f"Invalid or corrupted file.\n{e}"
            )

        return True, "Validation successful."


validator = FileValidator()
