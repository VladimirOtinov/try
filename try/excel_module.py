from PyQt6.QtWidgets import QFileDialog

class ExcelModule:
    def __init__(self, db_module):
        self.db_module = db_module

    def export_data_to_excel(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.ReadOnly

        filename, _ = QFileDialog.getSaveFileName(
            None,
            "Сохранить в Excel",
            "",
            "Excel Files (*.xlsx)",
            options=options
        )

        if filename:
            self.db_module.export_to_excel(filename)
