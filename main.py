import psycopg2
from employees.class_hh import HHManager
from vacancies.class_vacancy import VacancyManager
from utils.user_input import user_input
from db_classes.builder import DBBuilder
from db_classes.manager import DBManager


def main():
    print('Запуск программы. . .')

    hh_manager = HHManager()
    vacancy_manager = VacancyManager()

    companies_list = user_input()

    db_builder = DBBuilder(input("Введите название базы данных\n"))
    db_manager = DBManager(db_builder.name)

    db_builder.create_database()
    db_builder.create_tables()

    for company in companies_list:
        employee_data = hh_manager.get_employee_data(company)
        employee_id = hh_manager.get_employee_id(employee_data)
        hh_manager.save_as_csv(employee_data)

        vacancy_data = vacancy_manager.get_vacancy_data(employee_id)
        vacancy_manager.save_as_csv(vacancy_data)

        employees_data = db_manager.get_csv('employee.csv')
        vacancies_data = db_manager.get_csv('vacancy.csv')

        db_manager.insert_data(employees_data, vacancies_data)

    while True:
        print("""База данных готова для использования. Выберите необходимое действие:
        1 - Вывод компаний и количества их вакансий
        2 - Вывод всех вакансий с указанием компании, ссылки на вакансию и зарплату
        3 - Вывод средней зарплаты по вакансиям
        4 - Вывод вакансий с зарплатой выше среднего
        5 - Вывод всех вакансий, в названии которых содержится ключевое слово
        6 - Выход""")

        user_query = int(input())

        if user_query == 1:
            db_manager.get_companies_and_vacancies_count()

        elif user_query == 2:
            db_manager.get_all_vacancies()

        elif user_query == 3:
            db_manager.get_avg_salary()

        elif user_query == 4:
            db_manager.get_vacancies_with_higher_salary()

        elif user_query == 5:
            db_manager.get_vacancies_with_keyword()

        elif user_query == 6:
        #    db_manager.destroy()
            quit()


main()
