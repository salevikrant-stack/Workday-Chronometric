def load(self, file_path):

    from core.file_validator import validator

    valid, message = validator.validate(file_path)

    if not valid:
        raise Exception(message)

    self.file_path = Path(file_path)

    suffix = self.file_path.suffix.lower()

    self.dataframes.clear()

    self.sheet_names.clear()

    if suffix == ".csv":

        df = pd.read_csv(self.file_path)

        self.dataframes["Sheet1"] = df

        self.sheet_names = ["Sheet1"]

        return True

    workbook = pd.ExcelFile(self.file_path)

    self.sheet_names = workbook.sheet_names

    for sheet in self.sheet_names:

        self.dataframes[sheet] = pd.read_excel(
            self.file_path,
            sheet_name=sheet
        )

    return True
