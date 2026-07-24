from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import pandas as pd


@dataclass
class WorkbookInfo:
    file_name: str = ""
    file_path: str = ""
    sheet_names: List[str] = field(default_factory=list)
    active_sheet: str = ""


class DataModel:
    """
    Central Data Store

    Every module reads from this class.

    Excel is loaded ONCE.
    Dashboard, Reports, Leave,
    Overtime etc. all use the
    cached DataFrames.
    """

    def __init__(self):

        self.clear()

    ######################################################

    def clear(self):

        self.workbook = WorkbookInfo()

        self.frames: Dict[str, pd.DataFrame] = {}

        self.is_loaded = False

    ######################################################

    def load_workbook(
        self,
        file_name: str,
        file_path: str,
        sheets: Dict[str, pd.DataFrame]
    ):

        self.clear()

        self.workbook.file_name = file_name
        self.workbook.file_path = file_path

        self.frames = sheets

        self.workbook.sheet_names = list(sheets.keys())

        if self.workbook.sheet_names:
            self.workbook.active_sheet = self.workbook.sheet_names[0]

        self.is_loaded = True

    ######################################################

    def dataframe(self, sheet: Optional[str] = None):

        if not self.is_loaded:
            return None

        if sheet is None:
            sheet = self.workbook.active_sheet

        return self.frames.get(sheet)

    ######################################################

    def set_active_sheet(self, sheet):

        if sheet in self.frames:
            self.workbook.active_sheet = sheet

    ######################################################

    def active_sheet(self):

        return self.workbook.active_sheet

    ######################################################

    def sheet_names(self):

        return self.workbook.sheet_names

    ######################################################

    def row_count(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return 0

        return len(df)

    ######################################################

    def column_count(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return 0

        return len(df.columns)

    ######################################################

    def column_names(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return []

        return list(df.columns)

    ######################################################

    def head(self, rows=10, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return None

        return df.head(rows)

    ######################################################

    def statistics(self, sheet=None):

        df = self.dataframe(sheet)

        if df is None:
            return None

        return df.describe(include="all")

    ######################################################

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

    ######################################################

    def summary(self):

        if not self.is_loaded:
            return {}

        info = {}

        for name, df in self.frames.items():

            info[name] = {
                "rows": len(df),
                "columns": len(df.columns),
                "memory_mb": round(
                    df.memory_usage(deep=True).sum() / 1024 / 1024,
                    2,
                ),
            }

        return info


data_model = DataModel()
