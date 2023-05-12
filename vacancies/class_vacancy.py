import requests
import csv
from employees.class_hh import HHManager


class VacancyManager:
    """Класс для сбора информации о вакансиях"""
    __vacancy_url = 'https://api.hh.ru/vacancies'

    def get_vacancy_data(self, id: str) -> list[dict]:
        """
        Метод для получения информации о вакансиях
        :param id: ID компании, которое используется для поиска вакансий
        :return: Полученная информация о вакансиях (список словарей)
        """
        params = {
            "employer_id": id,
            "page": 5,
            "per_page": 100
        }

        response = requests.get(self.__vacancy_url, params=params).json()['items']

        return response

    @staticmethod
    def save_as_csv(datas: list[dict]) -> None:
        """
        Сохранение вакансий в .csv файл
        :param datas: Список словарей, содержащий информацию о вакансиях
        :return: Nothing :)
        """
        file_name = "vacancy.csv"

        with open(file_name, 'w', newline='', encoding='UTF-8') as file:
            fieldnames = ['id', 'title', 'url', 'salary_from', 'salary_to']

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for data in datas:
                if data['salary'] is None:
                    salary_from = 0
                    salary_to = 0
                else:
                    salary_from = 0 if data['salary']['from'] is None else data['salary']['from']
                    salary_to = 0 if data['salary']['to'] is None else data['salary']['to']

                writer.writerow({
                    'id': int(data['employer'].get('id')),
                    'title': str(data.get('name')),
                    'url': str(data.get('alternate_url')),
                    'salary_from': f'{float(salary_from)}',
                    'salary_to': f'{float(salary_to)}',
                })
