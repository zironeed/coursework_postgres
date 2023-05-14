from employees.class_hh import HHManager
from vacancies.class_vacancy import VacancyManager
from utils.user_input import user_input
from db_classes.builder import DBBuilder
from db_classes.manager import DBManager


if __name__ == '__main__':
    print('Запуск программы. . .')

    hh_manager = HHManager()
    vacancy_manager = VacancyManager()

    companies_list = user_input()

    db_builder = DBBuilder(input("Введите название базы данных"))
    db_manager = DBManager()

    db_builder.create_database()
    db_builder.create_tables()

    db_name = db_builder.name

    for company in companies_list:
        employee_data = hh_manager.get_employee_data(company)
        employee_id = hh_manager.get_employee_id(employee_data)
        hh_manager.save_as_csv(employee_data)

        vacancy_data = vacancy_manager.get_vacancy_data(employee_id)
        vacancy_manager.save_as_csv(vacancy_data)

        employees_data = db_manager.get_csv() #Путь до емплоес
        vacancies_data = db_manager.get_csv() #Путь до вакансиес

        db_manager.insert_data(db_name, employees_data, vacancies_data)
