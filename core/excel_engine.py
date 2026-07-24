from pathlib import Path
import pandas as pd

from core.file_validator import validator
from core.data_model import data_model


class ExcelEngine:
    """
    Enterprise Excel Processing Engine

    Supports:
        • .xlsx
        • .xls
        • .csv

    Features:
        • Validation
        • Multiple sheets
        • Cached DataFrames
        • Search
        • Summary
        • Reload
        • Export
    """

    def __init__(self):

        self.file_path = None

        self.sheet_names = []

        self.dataframes = {}

    ############################################################

    def load(self, file_path):

        valid, message = validator.validate(file_path)

        if not valid:
            raise Exception(message)

        self.file_path = Path(file_path)

        self.sheet_names.clear()
        self.dataframes.clear()

        suffix = self.file_path.suffix.lower()

        # CSV
        if suffix == ".csv":

            df = pd.read_csv(self.file_path)

            self.dataframes["Sheet1"] = df

            self.sheet_names.append("Sheet1")

        else:

            workbook = pd.ExcelFile(self.file_path)

            self.sheet_names = workbook.sheet_names

            for sheet in self.sheet_names:

                df = pd.read_excel(
                    self.file_path,
                    sheet_name=sheet
                )

                self.dataframes[sheet] = df

        data_model.load_workbook(
            file_name=self.file_path.name,
            file_path=str(self.file_path),
            sheets=self.dataframes
        )

        return True

    ############################################################

    def reload(self):

        if self.file_path is None:
            return False

        return self.load(self.file_path)

    ############################################################

    def dataframe(self, sheet=None):

        if sheet is None:

            if len(self.sheet_names) == 0:
                return None

            sheet = self.sheet_names[0]

        return self.dataframes.get(sheet)

    ############################################################

    def get_sheet_names(self):

        return self.sheet_names

    ############################################################

    def row_count(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return 0

        return len(df)

    ############################################################

    def column_count(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return 0

        return len(df.columns)

    ############################################################

    def columns(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return []

        return list(df.columns)

    ############################################################

    def head(self, rows=10, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return None

        return df.head(rows)

    ############################################################

    def tail(self, rows=10, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return None

        return df.tail(rows)

    ############################################################

    def summary(self):

        info = {}

        for sheet, df in self.dataframes.items():

            info[sheet] = {
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns),
                "memory_mb": round(
                    df.memory_usage(deep=True).sum() / 1024 / 1024,
                    2
                )
            }

        return info

    ############################################################

    def search(self, text, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return None

        mask = df.astype(str).apply(
            lambda col: col.str.contains(
                str(text),
                case=False,
                na=False
            )
        ).any(axis=1)

        return df[mask]

    ############################################################

    def export_csv(
        self,
        output_file,
        sheet=None
    ):

        df = self.dataframe(sheet)

        if df is None:
            return False

        df.to_csv(
            output_file,
            index=False
        )

        return True

    ############################################################

    def export_excel(
        self,
        output_file
    ):

        with pd.ExcelWriter(output_file) as writer:

            for sheet, df in self.dataframes.items():

                df.to_excel(
                    writer,
                    sheet_name=sheet,
                    index=False
                )

        return True

    ############################################################

    def workbook_name(self):

        if self.file_path is None:
            return ""

        return self.file_path.name

    ############################################################

    def workbook_path(self):

        if self.file_path is None:
            return ""

        return str(self.file_path)

    ############################################################

    def is_loaded(self):

        return len(self.dataframes) > 0

    ############################################################

    def close(self):

        self.file_path = None

        self.sheet_names.clear()

        self.dataframes.clear()

        data_model.clear()


excel_engine = ExcelEngine()
