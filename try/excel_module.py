import xlsxwriter

class ExcelModule:
    def export_data_to_excel(self, filename, data):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet("Cars")

        for row, rowData in enumerate(data, start=1):
            for col, value in enumerate(rowData):
                worksheet.write(row, col, value)

        workbook.close()
