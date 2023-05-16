import psycopg2


class DBBuilder:
    """Класс для создания БД и таблиц"""
    def __init__(self, db_name: str) -> None:
        self.__db_name = db_name

    def create_database(self) -> None:
        """
        Создание базы данных
        """
        print('Создание базы данных. . .')

        conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345", host="localhost")
        cursor = conn.cursor()

        conn.autocommit = True

        query = f'CREATE DATABASE {self.__db_name}'
        cursor.execute(query)

        cursor.close()
        conn.close()

        print(f'База данных {self.__db_name} создана.')

    def create_tables(self) -> None:
        """
        Создание таблиц employees и vacancies
        """
        print("Создание таблиц. . .")

        conn = psycopg2.connect(dbname=f"{self.__db_name}", user="postgres", password="12345", host="localhost")
        cursor = conn.cursor()

        conn.autocommit = True

        query_employee = "CREATE TABLE employees (" \
                         "id int PRIMARY KEY," \
                         "title varchar NOT NULL," \
                         "url varchar NOT NULL," \
                         "vacancy_count int)"

        query_vacancy = "CREATE TABLE vacancies (" \
                        "employee_id int REFERENCES employees (id)," \
                        "title varchar NOT NULL," \
                        "url varchar NOT NULL," \
                        "salary_from float," \
                        "salary_to float)"

        cursor.execute(query_employee)
        cursor.execute(query_vacancy)

        cursor.close()
        conn.close()

        print("Создание таблиц завершено.")

    @property
    def name(self):
        """Возвращает имя базы данных"""
        return self.__db_name
