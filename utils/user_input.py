def user_input():
    """
    Ввод пользователем интересующих его компаний
    :return: Список компаний
    """
    while True:
        input_in_str = input('Введите через запятую интересующие вас компании (10 компаний)\n')
        companies_list = input_in_str.split(', ')

        if len(companies_list) < 10 or len(companies_list) > 10:
            print(f'Введите 10 интересующих вас компаний (было введено {len(companies_list)} названий)\n')
            continue

        else:
            print('Поиск по следующим компаниям:', end=' ')
            print(*companies_list, sep=', ')
            return companies_list
