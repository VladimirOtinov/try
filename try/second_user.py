from PyQt6.QtWidgets import QDialog, QTableView, QTableWidgetItem, QTableWidget, QPushButton, QVBoxLayout, QHBoxLayout
class User_2(QDialog):
    def __init__(self):
        super(User_2, self).__init__()
        self.intUI()

    def f_unload(self):
        pass

    def click (self):
        temp = []
        with open ('workshop', 'r', encoding='utf-8') as f:
            for line in f:
                temp.append(line.split())
        self.table.setRowCount(len(temp))
        self.table.setColumnCount(len(temp[0]))
        for x in range(len(temp)):
            for i in range(len(temp[0])):
                self.table.setItem(x, i, QTableWidgetItem(temp[x][i]))
    def intUI(self):
        self.setWindowTitle('Список товаров в магазине')

        self.table = QTableWidget()

        self.btn_download = QPushButton('Загрузить')
        self.btn_sort_down = QPushButton('По убыванию')
        self.btn_sort_up = QPushButton('По возростанию')
        self.btn_unload = QPushButton('Отобразить данные в Excel')

        self.layout_all = QVBoxLayout()
        self.laouyt_btn = QHBoxLayout()

        self.laouyt_btn.addWidget(self.btn_download)
        self.laouyt_btn.addWidget(self.btn_unload)
        self.laouyt_btn.addWidget(self.btn_sort_down)
        self.laouyt_btn.addWidget(self.btn_sort_up)

        self.layout_all.addWidget(self.table)
        self.layout_all.addLayout(self.laouyt_btn)

        self.setLayout(self.layout_all)

        self.btn_download.clicked.connect(self.click)
        self.btn_unload.clicked.connect(self.f_unload)


