from employees.class_hh import HHManager
from vacancies.class_vacancy import VacancyManager
from utils.user_input import user_input


if __name__ == '__main__':
    print('Запуск программы. . .')

    hh_manager = HHManager()
    vacancy_manager = VacancyManager()

    companies_list = user_input()

    for company in companies_list:
        employee_data = hh_manager.get_employee_data(company)
        employee_id = hh_manager.get_employee_id(employee_data)
        hh_manager.save_as_csv(employee_data)

        vacancy_data = vacancy_manager.get_vacancy_data(employee_id)
        vacancy_manager.save_as_csv(vacancy_data)
