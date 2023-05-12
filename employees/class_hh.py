import requests
import csv


class HHManager:
    """Класс для сбора информации о компании"""
    __employee_url = 'https://api.hh.ru/employers?only_with_vacancies=true'

    def get_employee_data(self, company: str) -> list[dict]:
        """
        Метод для получения информации о компании
        :param company: Ключевое слово (название компании), которое используется для поиска
        :return: Полученная информация о компании (список словарей)
        """
        params = {
            "text": company.lower(),
            "per_page": 10,
            'area': 113
        }

        response = requests.get(self.__employee_url, params=params).json()['items']

        return response

    @staticmethod
    def get_employee_id(company: str, datas: list[dict]) -> str:
        """
        Метод для получения ID компании
        :param company: Название компании
        :param datas: Список словарей, из которого нужно достать ID
        :return: ID компании
        """
        for data in datas:
            if data['name'].lower() == company.lower():
                return data['id']

    @staticmethod
    def save_as_csv(datas: list[dict]) -> None:
        """
        Сохранение информации о компании в виде .csv файла
        :param file_name: Имя файла
        :param datas: Информация о компании
        :return: Nothing :)
        """
        file_name = "employee.csv"

        with open(file_name, 'w', newline='', encoding='UTF-8') as file:
            fieldnames = ['id', 'title', 'url', 'vacancy_count']

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for data in datas:
                writer.writerow({
                    'id': int(data.get('id')),
                    'title': str(data.get('name')),
                    'url': str(data.get('alternate_url')),
                    'vacancy_count': int(data.get('open_vacancies'))
                })
    