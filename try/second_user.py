from PyQt6.QtWidgets import QDialog, QTableView, QTableWidgetItem, QTableWidget, QPushButton, QVBoxLayout, QHBoxLayout
class User_2(QDialog):
    def __init__(self):
        super(User_2, self).__init__()
        self.intUI()

    def click(self):
        temp = []
        with open('workshop', 'r', encoding='utf-8') as f:
            for line in f:
                temp.append(line.split())
        print(temp)
        self.table.setRowCount(len(temp))
        self.table.setColumnCount(len(temp[0]))  # Используйте len(temp[0]) для количества столбцов

        for x in range(len(temp)):
            for i in range(len(temp[0])):  # Используйте len(temp[0]) для количества столбцов
                self.table.setItem(x, i, QTableWidgetItem(temp[x][i]))

    def intUI(self):
        self.setWindowTitle('Список товаров в магазине')

        self.table = QTableWidget()

        self.btn_download = QPushButton('Загрузить')

        self.layout_all = QVBoxLayout()

        self.layout_all.addWidget(self.table)
        self.layout_all.addWidget(self.btn_download)

        self.setLayout(self.layout_all)

        self.btn_download.clicked.connect(self.click)


