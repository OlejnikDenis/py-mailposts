import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from loguru import logger

import UI
from databasemanager import DatabaseManager


class CurrentSession:
    def __init__(self):
        """
        Класс реализует простую систему сессий
        """
        logger.info('User session initialized')
        self.UserName = None
        self.bUserAuthorized = False


class RowsWindow(QtWidgets.QMainWindow, UI.Ui_AddRowsWindow):
    def __init__(self):
        """
        Данный класс позволяет добавлять новые строки в БД
        """
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.append_data)

        # Здесь создаются валидаторы, запрещающие вводить что-то кроме цифр в соответствующих полях
        self.onlyInt = QIntValidator()
        self.LE_Index.setValidator(self.onlyInt)
        self.LE_Customers.setValidator(self.onlyInt)

    def keyPressEvent(self, event) -> None:
        """Расширение базового метода с целью упрощения добавления данных"""
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.append_data()
            event.accept()

    def append_data(self):
        """Метод позволяет добавлять новые данные в БД"""

        # Записываем текущие данные из полей для ввода в память
        subject_name = self.LE_SubjectName.text()
        city_name = self.LE_CityName.text()
        zipcode = self.LE_Index.text()
        customers = self.LE_Customers.text()

        query = f"INSERT INTO mailposts ('subject_name', 'city_name', 'zipcode', 'customers') " \
                f"VALUES ('{subject_name}', '{city_name}', '{zipcode}', '{customers}');"

        # Проверяем, есть ли введённый почтовый индекс уже в БД
        zipcode_founded = len(database.execute_read_query(f"SELECT * FROM mailposts WHERE zipcode='{zipcode}'"))
        if not zipcode_founded:

            # Проверяем на заполненность всех полей, иначе выдаём ошибку
            if subject_name and city_name and zipcode and customers:
                database.execute_write_query(query)
                logger.info('Row successfully added!')

                # Записываем данные в БД и обнуляем ввод пользователя
                self.LE_SubjectName.setText('')
                self.LE_CityName.setText('')
                self.LE_Index.setText('')
                self.LE_Customers.setText('')

                # Обновляем таблицу
                StartWindow.table_widget_init()
            else:
                self.errorWindow = ErrorWindow("Ошибка:\nНе все поля заполнены корректно")
                self.errorWindow.show()
        else:
            self.errorWindow = ErrorWindow("Ошибка со стороны базы данных:\nВведён уже имеющийся индекс")
            self.errorWindow.show()


class EditRowsWindow(QtWidgets.QMainWindow, UI.Ui_EditRowsWindow):
    def __init__(self, selected_row_zipcode):
        """Класс позволяет динамически редактировать БД"""
        super().__init__()
        self.setupUi(self)

        self.pushButton_EditRow.clicked.connect(self.edit_rowdata)

        # Здесь создаются валидаторы, запрещающие вводить что-то кроме цифр в соответствующих полях
        self.LE_EditRow_Zipcode.setValidator(QIntValidator())
        self.LE_EditRow_Customers.setValidator(QIntValidator())

        # Получаем информацию из БД на основе выбранной строки (её передаём в конструктор класса как параметр)
        data = database.execute_read_query_dict(f"SELECT * FROM mailposts WHERE zipcode = {selected_row_zipcode}")

        # Значения из БД записываем в поля для ввода с целью упрощения редактирования существующих данных
        self.LE_EditRow_SubjectName.setText(str(data[0]['subject_name']))
        self.LE_EditRow_CityName.setText(str(data[0]['city_name']))
        self.LE_EditRow_Zipcode.setText(str(data[0]['zipcode']))
        self.LE_EditRow_Customers.setText(str(data[0]['customers']))

    def edit_rowdata(self):
        """Метод заменяет старые данные на новые только что введённые"""

        # Записываем текущие изменения в память
        subject_name = self.LE_EditRow_SubjectName.text()
        city_name = self.LE_EditRow_CityName.text()
        zipcode = self.LE_EditRow_Zipcode.text()
        customers = self.LE_EditRow_Customers.text()

        query_add = f"INSERT INTO mailposts ('subject_name', 'city_name', 'zipcode', 'customers') " \
                    f"VALUES ('{subject_name}', '{city_name}', '{zipcode}', '{customers}');"
        query_del = f"DELETE FROM mailposts WHERE zipcode='{zipcode}'"

        # Если все поля заполнены
        if subject_name and city_name and zipcode and customers:
            # То удаляем строку из БД и сразу же заполняем её новыми данными
            database.execute_write_query(query_del)
            database.execute_write_query(query_add)

            logger.info(f'Succesfully changed row with zipcode "{zipcode}"')

            # Обновляем таблицу
            StartWindow.table_widget_init()
        else:
            self.errorWindow = ErrorWindow("Ошибка:\nНе все поля заполнены корректно")
            self.errorWindow.show()

    def keyPressEvent(self, event) -> None:
        """Расширение базового метода с целью упрощения редактирования данных"""
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.edit_rowdata()
            event.accept()


class AuthWindow(QtWidgets.QMainWindow, UI.Ui_AuthWindow):
    def __init__(self):
        """Данный класс реализует окно авторизации пользователя"""
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.validate_auth_data)

    # Вызывается по нажатию кнопки авторизации либо 'enter'
    def validate_auth_data(self):
        # Берём введённые значения для авторизации
        login = self.Input_Login.text()
        password = self.Input_Pass.text()

        # Делаем запрос к БД с нашими данными
        query = f'SELECT * FROM users WHERE login="{login}" AND password="{password}";'
        data = database.execute_read_query(query)

        if data:
            # Если такой логин/пароль найден, то записываем данные в класс Session
            logger.info(f'User ({data[0][0]}) is successfully logged on!')

            session.bUserAuthorized = True
            session.UserName = login

            self.close()
        else:
            logger.error('User authorization error!')
            session.bUserAuthorized = False

            self.errorWindow = ErrorWindow("Ошибка входа:\nНеверный логин или пароль!")
            self.errorWindow.show()

    def keyPressEvent(self, event) -> None:
        """Расширение базового метода с целью упрощения авторизации"""
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.validate_auth_data()
            event.accept()


class ErrorWindow(QtWidgets.QWidget, UI.Ui_ErrorDialog):
    def __init__(self, message: str):
        """Данный класс представляет собой окно с ошибкой. Значение ошибки передаётся в конструктор"""
        super().__init__()
        self.setupUi(self)
        self.label.setText(message)
        self.pushButton_closeErrWindow.clicked.connect(self.close_window)

    def keyPressEvent(self, event) -> None:
        """Расширение базового метода с целью упрощения закрытия окна с ошибкой"""
        if event.key() == QtCore.Qt.Key.Key_Return:
            self.close_window()
            self.close()

    def close_window(self):
        self.close()


class MainWindow(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        """Основной класс, представляющий собой главный интерфейс программы"""
        logger.debug('New window: Main')
        super().__init__()
        self.setupUi(self)

        # TODO : HIDE
        self.L_SubjectTypeTitle.hide()
        self.checkBox_Type_AutonomousRegion.hide()
        self.checkBox_Type_AutonomousDistrict.hide()
        self.checkBox_Type_FederalCity.hide()
        self.checkBox_Type_Region.hide()
        self.checkBox_Type_Area.hide()
        self.checkBox_Type_Republic.hide()
        self.LE_Stats_Cities.hide()
        self.LE_Stats_Customers.hide()
        self.LE_Stats_AvgCustomers.hide()
        self.LE_Stats_UniqueSubjects.hide()

        # Настройка TableWidget
        self.tableWidget.setColumnWidth(0, 175)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setSortingEnabled(True)

        # Подключение кнопок...
        # ...авторизации
        self.MenuBar_Login.triggered.connect(self.menubar_auth)
        self.MenuBar_Exit.triggered.connect(self.menubar_exit)

        # ...фильтров
        self.checkBox_Type_AutonomousRegion.toggled.connect(self.get_active_filters)
        self.checkBox_Type_AutonomousDistrict.toggled.connect(self.get_active_filters)
        self.checkBox_Type_FederalCity.toggled.connect(self.get_active_filters)

        self.checkBox_Type_Region.toggled.connect(self.get_active_filters)
        self.checkBox_Type_Area.toggled.connect(self.get_active_filters)
        self.checkBox_Type_Republic.toggled.connect(self.get_active_filters)

        self.pushButton_Find.clicked.connect(self.search_by_filters)
        self.pushButton_Reset.clicked.connect(self.search_reset)

        # ...редактирования данных
        self.pushButton_RowAdd.clicked.connect(self.add_row)
        self.pushButton_RowEdit.clicked.connect(self.edit_row)
        self.pushButton_RowDel.clicked.connect(self.delete_row)

        # Базовые методы и поля инициализации
        self.table_widget_init()
        self.filters = dict()

    def get_active_filters(self) -> dict:
        """Метод возвращает словарь со всеми активными фильтрами"""
        """
        self.filters['check_AutonomousRegion'] = self.checkBox_Type_AutonomousRegion.isChecked()
        self.filters['check_AutonomousDistrict'] = self.checkBox_Type_AutonomousDistrict.isChecked()
        self.filters['check_FederalCity'] = self.checkBox_Type_FederalCity.isChecked()
        self.filters['check_Region'] = self.checkBox_Type_Region.isChecked()
        self.filters['check_Area'] = self.checkBox_Type_Area.isChecked()
        self.filters['check_Republic'] = self.checkBox_Type_Republic.isChecked()
        """
        # self.filters['SubjectName'] = self.comboBox_SubjectName.currentText()
        self.filters['SubjectName'] = self.comboBox_SubjectName.text()
        self.filters['CityName'] = self.comboBox_CityName.text()
        self.filters['Zipcode'] = self.comboBox_Index.text()

        return self.filters

    def search_by_filters(self):
        """Данный метод производит поиск по активным фильтрам"""
        self.get_active_filters()
        params = list()
        any_selected: bool = False
        """
        if self.filters['check_AutonomousRegion']:
            params.append(f"instr(subject_name, 'автономная')")
        if self.filters['check_AutonomousDistrict']:
            params.append(f"instr(subject_name, 'округ')")
        if self.filters['check_FederalCity']:
            params.append(f"instr(subject_name, 'федерального')")
        if self.filters['check_Region']:
            params.append(f"instr(subject_name, 'край')")
        if self.filters['check_Area']:
            params.append(f"instr(subject_name, 'область')")
        if self.filters['check_Republic']:
            params.append(f"(instr(subject_name, 'республика') OR instr(subject_name, 'Республика'))")
        """

        # Проверяем каждый доступный фильтр:
        if self.filters['SubjectName']:
            any_selected = True
            params.append(f"(instr(subject_name, '{self.filters['SubjectName'].capitalize()}') OR instr(subject_name, '{self.filters['SubjectName'].lower()}'))")
        if self.filters['CityName']:
            any_selected = True
            params.append(f"(instr(city_name, '{self.filters['CityName'].capitalize()}') OR instr(city_name, '{self.filters['CityName'].lower()}'))")
        if self.filters['Zipcode']:
            any_selected = True
            params.append(f"instr(zipcode, '{self.filters['Zipcode']}')")

        # Динамически добавляем в середину списка sql-параметр 'and' для успешного выполнения запроса
        result = [' AND '] * (len(params) * 2 - 1)
        result[0::2] = params

        # Выполняем запрос, если хоть один параметр активен
        query = f"SELECT * FROM mailposts WHERE {''.join(result)};"
        if any_selected:
            filtered_data = database.execute_read_query_dict(query)

            # Обновляем таблицу на основе данных полученный из БД
            self.table_widget_update(filtered_data)

    def search_reset(self):
        """Метод обнуляет все активные фильтры, а так же обновляет таблицу"""
        """
        self.checkBox_Type_AutonomousRegion.setChecked(False)
        self.checkBox_Type_AutonomousDistrict.setChecked(False)
        self.checkBox_Type_FederalCity.setChecked(False)
        self.checkBox_Type_Region.setChecked(False)
        self.checkBox_Type_Area.setChecked(False)
        self.checkBox_Type_Republic.setChecked(False)
        """
        self.comboBox_SubjectName.setText('')
        self.comboBox_CityName.setText('')
        self.comboBox_Index.setText('')

        # Обновление таблицы
        self.get_active_filters()
        self.table_widget_init()

    def add_row(self):
        """Метод создаёт новое окно добавления данных"""
        if session.bUserAuthorized:
            logger.debug("New window: AddRowsWindow")
            self.AddRowsWindow = RowsWindow()
            self.AddRowsWindow.show()
        else:
            logger.warning('You are not logged in.')
            self.errorWindow = ErrorWindow("Ошибка:\nВы не авторизованы как администратор")
            self.errorWindow.show()

    def edit_row(self):
        """Метод позволяет редактировать раннее созданные строчки в БД"""
        if session.bUserAuthorized:

            # Если пользователь выбрал хотя бы одну строку:
            if self.tableWidget.currentRow() > -1:
                # Выделяем из строки zipcode - это наш Primary Key для взаимодействия
                selected_row_zipcode = self.tableWidget.item(self.tableWidget.currentRow(), 2).text()

                # Если zipcode (индекс почтового отделения) существует, то создаём новое окно редактора
                if selected_row_zipcode:
                    logger.debug("New window: AddRowsWindow")

                    self.EditRowsWindow = EditRowsWindow(selected_row_zipcode)
                    self.EditRowsWindow.show()
            else:
                logger.warning('The row was not selected')
                self.errorWindow = ErrorWindow("Строка не выбрана")
                self.errorWindow.show()
        else:
            logger.warning('You are not logged in.')
            self.errorWindow = ErrorWindow("Ошибка:\nВы не авторизованы как администратор")
            self.errorWindow.show()

    def delete_row(self):
        """Метод удаляет выделенные строчки из БД"""
        try:
            if session.bUserAuthorized:
                selected_row = self.tableWidget.currentRow()

                # Если выбрана хотя бы одна строка:
                if selected_row > -1:
                    # Выделяем из строки zipcode - это наш Primary Key для взаимодействия
                    selected_item_zipcode = self.tableWidget.item(selected_row, 2).text()

                    # Удаляем строку на основе указанного индекса (zipcode)
                    query = f"DELETE FROM mailposts WHERE zipcode = '{selected_item_zipcode}'"
                    database.execute_write_query(query)

                    logger.info(f'Succesfully deleted row with zipcode "{selected_item_zipcode}"')
                    # Обновляем таблицу
                    self.table_widget_init()
                else:
                    logger.warning('The row was not selected')
                    self.errorWindow = ErrorWindow("Строка для удаления не выбрана")
                    self.errorWindow.show()
            else:
                logger.warning('You are not logged in.')
                self.errorWindow = ErrorWindow("Ошибка:\nВы не авторизованы как администратор")
                self.errorWindow.show()
        except Exception as err:
            logger.exception(err)

    def menubar_auth(self):
        """Метод из меню. Вызывается при попытке авторизации пользователя"""
        logger.debug("New window: Authorization")
        self.AuthWindow = AuthWindow()
        self.AuthWindow.show()

    def menubar_exit(self):
        """Вызывается когда нажата кнопка 'выход'"""
        logger.info("'Exit' button triggered!")
        sys.exit()

    def update_stats(self, data):
        """Временный метод, используемый для получения сведений о текущем состоянии таблицы"""
        pass

        # Заготовки текста для вывода
        _UniqueSubjects = 'Уникальных субъектов: '
        _Mailposts = "Почтовых отделений: "
        _Customers = "Количество клиентов: "
        _Cities = "Населённых пунктов: "
        _AvgCustomers = "Ср. количество клиентов: "

        # Здесь создаются списки с уникальными значениями на основе данных из БД
        _UniqueSubjects_list = list(({item['subject_name']: item for item in data}.values()))
        _Mailposts_list = list(({item['zipcode']: item for item in data}.values()))
        _Customers_value = 0
        for row in data:
            _Customers_value += row['customers']

        _Cities_list = list(({item['city_name']: item for item in data}.values()))

        # Получаем целочисленнные данные для дальнейшего вывода
        _UniqueSubjects_value = len(_UniqueSubjects_list)
        _Mailposts_value = len(_Mailposts_list)
        _Cities_value = len(_Cities_list)
        if _Mailposts_value:
            _AvgCustomers_value = _Customers_value / _Mailposts_value
        else:
            _AvgCustomers_value = 0

        # Устанавливаем полученные данные с заготовленным текстом
        self.LE_Stats_UniqueSubjects.setText(_UniqueSubjects + str(_UniqueSubjects_value))
        self.LE_Stats_Mailposts.setText(_Mailposts + str(_Mailposts_value))
        self.LE_Stats_Customers.setText(_Customers + str(_Customers_value))
        self.LE_Stats_Cities.setText(_Cities + str(_Cities_value))
        self.LE_Stats_AvgCustomers.setText(_AvgCustomers + str(int(_AvgCustomers_value)))

    def table_widget_update(self, data: list):
        """Один из часто вызываемых методов. К нему общаются тогда, когда необходимо обновить таблицу с данными"""
        self.tableWidget.setRowCount(len(data))

        # На основе полученных данных проходимся по каждому элементу..
        for row_num, row in enumerate(data):
            item_index = QtWidgets.QTableWidgetItem()
            item_index.setData(Qt.EditRole, int(row['zipcode']))
            item_customers = QtWidgets.QTableWidgetItem()
            item_customers.setData(Qt.EditRole, int(row['customers']))

            # ... и устанавливаем его как 'item'-значение в нашей таблице.
            self.tableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(row['subject_name']))
            self.tableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row['city_name']))
            self.tableWidget.setItem(row_num, 2, item_index)
            self.tableWidget.setItem(row_num, 3, item_customers)

        logger.info('TableWidget updated!')
        self.update_stats(data)

    def table_widget_init(self):
        """Метод инициализации (первичного заполнения) таблицы. Вызывается из конструктора"""
        data = database.execute_read_query_dict('SELECT * FROM mailposts')
        self.table_widget_update(data)


if __name__ == '__main__':
    logger.start("log.txt")
    logger.info("Application started!")

    # Создаём ссылку на приложение
    app = QtWidgets.QApplication([])

    # Создаём объекты классов для дальнейшей работы с нимм
    session = CurrentSession()
    database = DatabaseManager()

    # Создаём окно и включаем отображение
    StartWindow = MainWindow()
    StartWindow.show()

    sys.exit(app.exec())

