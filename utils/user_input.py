def user_input() -> list:
    """
    Ввод пользователем интересующих его компаний
    :return: Список компаний
    """
    companies_list = []

    while True:
        company_name = input("Введите названия интересующих вас компаний (10 компаний). "
                             "Введите 'стоп', когда закончие ввод.\n")

        if company_name.lower() == 'стоп':
            print(f'Были введены следующие названия:')
            print(*companies_list, sep=', ')

            return companies_list

        companies_list.append(company_name)

        if len(companies_list) >= 10:
            print(f'Вы ввели максимальное количество компаний. Начинаю работу\n')
            print(f'Были введены следующие названия:')
            print(*companies_list, sep=', ')

            return companies_list
