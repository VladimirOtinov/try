import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog, QLineEdit, QLabel, QDialog
from db_module import DBModule
from excel_module import ExcelModule
from second_user import User_2
class ColorAndCarSelectionWindow(QDialog):
    def __init__(self, db_module, excel_module):
        super().__init__()

        self.setWindowTitle("Выбор цвета и данных автомобиля")
        self.layout = QVBoxLayout()

        self.color_dialog = QColorDialog()
        self.layout.addWidget(self.color_dialog)

        self.make_label = QLabel("Марка автомобиля:")
        self.make_input = QLineEdit()
        self.layout.addWidget(self.make_label)
        self.layout.addWidget(self.make_input)

        self.year_label = QLabel("Год производства:")
        self.year_input = QLineEdit()
        self.layout.addWidget(self.year_label)
        self.layout.addWidget(self.year_input)

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

    def get_color(self):
        return self.color_dialog.selectedColor().name()

    def get_make(self):
        return self.make_input.text()

    def get_year(self):
        return self.year_input.text()

    def get_country(self):
        return self.country_input.text()

    def save_to_db(self):
        selected_color = self.get_color()
        make = self.get_make()
        year = self.get_year()
        country = self.get_country()

        self.db_module.create_table()
        self.db_module.insert_car(make, year, selected_color, country)

    def export_to_excel(self):
        selected_color = self.get_color()
        self.excel_module.export_data_to_excel(selected_color)




class UserSelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выбор пользователей")
        self.setGeometry(100, 100, 300, 150)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.db_module = DBModule()
        self.excel_module = ExcelModule(self.db_module)

        self.select_user1_button = QPushButton("Выбрать пользователя 1")
        self.select_user1_button.clicked.connect(self.select_user1)
        layout.addWidget(self.select_user1_button)

        self.select_user2_button = QPushButton("Выбрать пользователя 2")
        self.select_user2_button.clicked.connect(self.select_user2)
        layout.addWidget(self.select_user2_button)

        self.central_widget.setLayout(layout)

    def select_user1(self):
        color_and_car_dialog = ColorAndCarSelectionWindow(self.db_module, self.excel_module)
        color_and_car_dialog.exec()

    def select_user2(self):
        dlg = User_2()
        dlg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserSelectionWindow()
    window.show()
    sys.exit(app.exec())
