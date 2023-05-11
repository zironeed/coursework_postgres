import requests
from site_class import abs_class


class HH(abs_class):
    """Класс для сайта hh.ru"""
    def __init__(self) -> None:
        self.__vacancies = []

    @property
    def vacancies(self) -> list:
        return self.__vacancies

    def get_request(self, keywords: str) -> None or str:
        """
        Запрос к ресурсу
        :param keywords: название вакансии для поиска
        :return: список с данными или None
        """
        print("Делаем запрос с HEAD HUNTER")
        url_head_hunter = "https://api.hh.ru/vacancies"
        page_number = 0
        # количество страниц обработки
        all_pages = 5

        while page_number < all_pages:

            params = {
                "text": keywords,
                "per_page": 100,
                "page": page_number,
            }

            response = requests.get(url_head_hunter, params=params)
            if response.status_code == 200:

                vacancies = response.json()["items"]
                for vacancy in vacancies:

                    # Обработка данных по заработной плате
                    if vacancy["salary"] is not None:
                        salary_from = vacancy["salary"]["from"]
                        if salary_from is None:
                            salary_from = 0
                        salary_to = vacancy["salary"]["to"]
                        if salary_to is None:
                            salary_to = 0
                    else:
                        salary_from = 0
                        salary_to = 0

                    # Обработка формата для поля responsibility/requirement
                    convert_responsibility = format_text(vacancy["snippet"]["responsibility"])
                    convert_requirement = format_text(vacancy["snippet"]["requirement"])

                    # получаем всю информацию по запросу
                    self.__vacancies.append({"name": (vacancy["name"]).lower(),
                                             "url": (vacancy["url"]).lower(),
                                             "responsibility": convert_responsibility.lower(),
                                             "town": (vacancy["area"]["name"]).lower(),
                                             "employer": (vacancy["employer"]["name"]).lower(),
                                             "requirement": convert_requirement.lower(),
                                             "salary_from": (str(salary_from)).lower(),
                                             "salary_to": (str(salary_to)).lower(),
                                             })
            else:
                return "Error:", response.status_code

            # для обработки информации на следующей странице (all_pages = response.json()["pages"])
            page_number += 1
    