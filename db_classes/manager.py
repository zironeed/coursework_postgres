import psycopg2
import csv


class DBManager:
    """Класс, используемый для работы с данными"""
    def get_csv(self, path: str) -> list:
        """Получение данных из .csv файла"""
        data = []
        count = 0

        with open(path) as csv_file:
            file = csv.reader(csv_file, delimiter=',')

            for line in file:
                if count != 0:
                    data.append(line)
                else:
                    count += 1

        return data

    def insert_data(self, name: str, args_emp: list, args_vac: list) -> None:
        """Внесение данных в БД"""
        print("Вношу данные в базу. . .")

        with psycopg2.connect(host='localhost', database=f'{name}', user='postgres', password='12345') as con:
            with con.cursor() as cur:
                count_emp = ''.join('%s,' * len(args_emp[0]))
                count_vac = ''.join('%s,' * len(args_vac[0]))

                query_employee = f"INSERT INTO employees VALUES ({count_emp[:-1]})"
                query_vacancies = f"INSERT INTO vacancies VALUES ({count_vac[:-1]})"

                cur.executemany(query_employee, args_emp)
                cur.executemany(query_vacancies, args_vac)

        con.close()

        print("Данные занесены в базу.")

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self, keyword: str):
        pass
