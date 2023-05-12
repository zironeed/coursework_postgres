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
        print(f'Сбор информации о {company}. . .')

        params = {
            "text": company.lower(),
            "per_page": 10,
            'area': 113
        }

        response = requests.get(self.__employee_url, params=params).json()['items']

        return response

    @staticmethod
    def get_employee_id(datas: list[dict]) -> list:
        """
        Метод для получения ID компании
        :param datas: Список словарей, из которого нужно достать ID
        :return: Список, содержащий ID компаний
        """
        id_list = []

        for data in datas:
            id_list.append(data['id'])

        return id_list

    @staticmethod
    def save_as_csv(datas: list[dict]) -> None:
        """
        Сохранение информации о компании в виде .csv файла
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

        print('Выполнено.')
    