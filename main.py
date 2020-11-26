import sys

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('coffee.sqlite')
        # И откроем подключение
        db.open()
        self.model = QSqlTableModel(self, db)
        self.model.setTable('coffee')
        self.model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        self.view.setModel(self.model)
        self.view.move(10, 10)
        self.view.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('Эспрессо')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())


# # Created by Sergey Yaksanov at 26.11.2020
# Copyright © 2020 Yakser. All rights reserved.
