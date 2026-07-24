from pathlib import Path
import pandas as pd


class ExcelEngine:
    """
    Central Excel Processing Engine

    Loads:
    - xlsx
    - xls
    - csv

    Returns pandas DataFrames.
    """

    def __init__(self):

        self.file_path = None

        self.workbook = None

        self.sheet_names = []

        self.dataframes = {}

    ############################################################

    def load(self, file_path):

        self.file_path = Path(file_path)

        suffix = self.file_path.suffix.lower()

        if suffix == ".csv":

            df = pd.read_csv(self.file_path)

            self.dataframes["Sheet1"] = df

            self.sheet_names = ["Sheet1"]

            return True

        excel = pd.ExcelFile(self.file_path)

        self.sheet_names = excel.sheet_names

        for sheet in self.sheet_names:

            self.dataframes[sheet] = pd.read_excel(
                self.file_path,
                sheet_name=sheet
            )

        return True

    ############################################################

    def get_sheet_names(self):

        return self.sheet_names

    ############################################################

    def dataframe(self, sheet):

        return self.dataframes.get(sheet)

    ############################################################

    def rows(self, sheet):

        if sheet not in self.dataframes:
            return 0

        return len(self.dataframes[sheet])

    ############################################################

    def columns(self, sheet):

        if sheet not in self.dataframes:
            return []

        return list(self.dataframes[sheet].columns)

    ############################################################

    def summary(self):

        info = {}

        for sheet, df in self.dataframes.items():

            info[sheet] = {
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns),
            }

        return info


excel_engine = ExcelEngine()
