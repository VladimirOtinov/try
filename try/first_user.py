from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QDialog

class ColorAndCarSelectionWindow(QDialog):
    def __init__(self, db_module, excel_module):
        super().__init__()

        self.setWindowTitle("Ввод данных автомобиля")
        self.layout = QVBoxLayout()

        self.make_label = QLabel("Марка автомобиля:")
        self.make_input = QLineEdit()
        self.layout.addWidget(self.make_label)
        self.layout.addWidget(self.make_input)

        self.year_label = QLabel("Год производства:")
        self.year_input = QLineEdit()
        self.layout.addWidget(self.year_label)
        self.layout.addWidget(self.year_input)

        self.color_label = QLabel("Цвет автомобиля:")
        self.color_input = QLineEdit()
        self.layout.addWidget(self.color_label)
        self.layout.addWidget(self.color_input)

        self.country_label = QLabel("Страна производителя:")
        self.country_input = QLineEdit()
        self.layout.addWidget(self.country_label)
        self.layout.addWidget(self.country_input)

        self.save_button = QPushButton("Сохранить в БД")
        self.save_button.clicked.connect(self.save_to_db)
        self.layout.addWidget(self.save_button)

        self.export_to_excel_button = QPushButton("Отобразить данные в Excel")
        self.export_to_excel_button.clicked.connect(self.export_to_excel)
        self.layout.addWidget(self.export_to_excel_button)

        self.setLayout(self.layout)

        self.db_module = db_module
        self.excel_module = excel_module

    def get_make(self):
        return self.make_input.text()

    def get_year(self):
        return self.year_input.text()

    def get_color(self):
        return self.color_input.text()

    def get_country(self):
        return self.country_input.text()

    def save_to_db(self):
        make = self.get_make()
        year = self.get_year()
        color = self.get_color()
        country = self.get_country()

        self.db_module.create_table()
        self.db_module.insert_car(make, year, color, country)

    def export_to_excel(self):
        color = self.get_color()
        self.excel_module.export_data_to_excel(color)
