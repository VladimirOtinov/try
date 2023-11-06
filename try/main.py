import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QColorDialog, QLineEdit, QLabel, QDialog
from db_module import DBModule
from excel_module import ExcelModule
from second_user import User_2
from first_user import ColorAndCarSelectionWindow

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
