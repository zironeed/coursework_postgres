import psycopg2
import csv


class DBManager:
    """Класс, используемый для работы с данными"""
    def __init__(self, name: str) -> None:
        self.__db_name = name

    @staticmethod
    def get_csv(path: str) -> list:
        """Получение данных из .csv файла"""
        data = []
        count = 0

        with open(path, encoding='utf-8') as csv_file:
            file = csv.reader(csv_file, delimiter=',')

            for line in file:
                if count != 0:
                    data.append(line)
                else:
                    count += 1

        return data

    def insert_data(self, args_emp: list, args_vac: list) -> None:
        """Внесение данных в БД"""
        print("Вношу данные в базу. . .")

        with psycopg2.connect(host='localhost', database=f'{self.__db_name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:
                count_emp = ''.join('%s,' * len(args_emp[0]))
                count_vac = ''.join('%s,' * len(args_vac[0]))

                query_employee = f"INSERT INTO employees VALUES ({count_emp[:-1]})"
                query_vacancies = f"INSERT INTO vacancies VALUES ({count_vac[:-1]})"

                cur.executemany(query_employee, args_emp)
                cur.executemany(query_vacancies, args_vac)

            cur.close()
        con.close()

        print("Данные занесены в базу.")

    def get_companies_and_vacancies_count(self) -> None:
        """Вывод компаний и количества их вакансий"""
        with psycopg2.connect(host='localhost', database=f'{self.__db_name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:

                query = f"SELECT title, vacancy_count FROM employees"
                cur.execute(query)
                result = cur.fetchall()

                for line in result:
                    print(line)

            cur.close()
        con.close()

    def get_all_vacancies(self) -> None:
        """Вывод всех вакансий с указанием компании, ссылки на вакансию и зарплату"""
        with psycopg2.connect(host='localhost', database=f'{self.__db_name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:

                query = """SELECT vacancies.title, employees.title, vacancies.url, vacancies.salary_from, 
                vacancies.salary_to FROM vacancies 
                JOIN employees ON vacancies.employee_id=employees.id"""
                cur.execute(query)
                result = cur.fetchall()

                for line in result:
                    print(line)

            cur.close()
        con.close()

    def get_avg_salary(self) -> None:
        """Вывод средней зарплаты по вакансиям"""
        with psycopg2.connect(host='localhost', database=f'{self.__db_name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:

                query = f"SELECT AVG((salary_from + salary_to)/2) AS average FROM vacancies"
                cur.execute(query)
                result = cur.fetchall()

                for line in result:
                    print(line)

            cur.close()
        con.close()

    def get_vacancies_with_higher_salary(self) -> None:
        """Вывод вакансий с зарплатой выше среднего"""
        with psycopg2.connect(host='localhost', database=f'{self.__db_name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:

                query = """SELECT title, salary_from, salary_to, url
                            FROM vacancies
                            WHERE salary_from > (SELECT AVG((salary_from + salary_to) / 2) FROM vacancies)
                            ORDER BY salary_from DESC"""
                cur.execute(query)
                result = cur.fetchall()

                for line in result:
                    print(line)

            cur.close()
        con.close()

    def get_vacancies_with_keyword(self) -> None:
        """Вывод всех вакансий, в названии которых содержатся переданные в метод слова"""
        keyword = input("Введите ключевое слово\n")

        with psycopg2.connect(host='localhost', database=f'{self.__db_name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:

                query = f"""SELECT * FROM vacancies 
                WHERE title LIKE '%{keyword}%'"""
                cur.execute(query)
                result = cur.fetchall()

                for line in result:
                    print(line)

            cur.close()
        con.close()

    #def destroy(self):
    #    """Удаление базы данных"""
    #    with psycopg2.connect(host='localhost', database=f'postgres', user='postgres', password='12345') as con:
    #        with con.cursor() as cur:
    #
    #            query = f"""SELECT pg_terminate_backend(pg_stat_activity.pid)
    #            FROM pg_stat_activity
    #            WHERE pg_stat_activity.datname = {self.__db_name}
    #            AND pid <> pg_backend_pid();"""
    #
    #            cur.execute(query)
    #
    #        cur.close()
    #    con.close()
