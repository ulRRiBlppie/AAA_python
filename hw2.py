def department_structure_info(myfile) -> None:
    '''
    Вход: открыйтый файл с заглавием
    Выход: None
    Функция печатает департаменты и команды внутри каждого департамента
    '''
    d = {'Департамент': {'Команды в департаменте'}}
    _ = myfile.readline()
    for line in myfile:
        read_line = line[:-1].split(';')
        if read_line[1] in d:
            d[read_line[1]].add(read_line[2])
        else:
            d[read_line[1]] = {read_line[2], }

    for department in d:
        print(f'{department}:', end='\t\t')
        print(*[el for el in d[department]], sep=', ')


def statistics_per_department(myfile) -> dict:
    '''
    Вход: открытый файл с заглавием
    Выход: словарь с ключами названиями департаментов
    и значениями в виде словарей, отображающие
    некоторые статистики каждого департамента
    '''
    d = {'Департамент': {'Сотрудники': [], 'Зарплаты': []}}
    _ = myfile.readline()
    for line in myfile:
        read_line = line[:-1].split(';')
        if read_line[1] in d:
            d[read_line[1]]['Сотрудники'].append(read_line[0])
            d[read_line[1]]['Зарплаты'].append(int(read_line[5]))
        else:
            d[read_line[1]] = {'Сотрудники': [read_line[0], ], 'Зарплаты': [int(read_line[5]), ]}

    all_departments = list(set([department for department in d if department != 'Департамент']))
    dict_with_all_info = {}
    for department in all_departments:
        dict_with_all_info[department] = {
                'Кол-во сотрудников': len(d[department]['Сотрудники']),
                'Минимальная зарплата': min(d[department]['Зарплаты']),
                'Максимальная зарплата': max(d[department]['Зарплаты']),
                'Средняя зарплата': sum(d[department]['Зарплаты'])/len(d[department]['Сотрудники'])}

    return dict_with_all_info


def statistics_per_department_print(myfile) -> None:
    '''
    Вход: открытый файл с заглавием
    Выход: словарь с ключами названиями департаментов
    и значениями в виде словарей, отображающие некоторые статистики каждого департамента
    '''
    d = statistics_per_department(myfile)
    print("Департамент: \
            \t Кол-во сотрудников\
            \t Минимальная--Максимальная зарплата\
            \t Средняя зарплата ")
    for department in d:

        print(f"{department}: \
            \t {d[department]['Кол-во сотрудников']}\
            \t {d[department]['Минимальная зарплата']}--{d[department]['Максимальная зарплата']}\
            \t {d[department]['Средняя зарплата']:.0f} ")


def statistics_per_department_csv(myfile) -> None:
    d = statistics_per_department(myfile)
    list_csv = []
    row_csv = []
    string_csv = ''
    for department in d:
        row_csv = [str(department), str(d[department]['Кол-во сотрудников']),
                   str(d[department]['Минимальная зарплата']) + '--' + str(d[department]['Максимальная зарплата']),
                   str(round(d[department]['Средняя зарплата'], 2))]

        list_csv.append(';'.join(row_csv))
    string_csv = '\n'.join(list_csv)

    with open('result.csv', 'w') as f:
        f.writelines(string_csv)

    return string_csv


def menu_call():
    '''
    Спрашивает у юзера, что ему нужно в формате {1, 2, 3}
    Возвращает число
    '''
    print(
        '1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него',
        '2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату',
        '3.Сохранить сводный отчёт из предыдущего пункта в виде csv-файла\n', sep='\n')
    print('Введите 1, 2 или 3')
    request_num = int(input())
    if request_num == 1 or request_num == 2 or request_num == 3:
        return request_num
    else:
        print('Ошибка')
        return menu_call()


def main_body(request_num: int, csv_file: str = 'Corp_Summary.csv'):
    '''
    Читает файл и выполняет функции согласно переданному числу
    '''
    myfile = open(csv_file, "r")

    if request_num == 1:
        department_structure_info(myfile)
    elif request_num == 2:
        statistics_per_department_print(myfile)
    elif request_num == 3:
        statistics_per_department_csv(myfile)


if __name__ == '__main__':
    complete_flg = False

    while not complete_flg:
        main_body(menu_call())
        print('1. Запустить программу еще раз', '2. завершить работу', sep='\n')
        print('Введите число 1, если вы хотите запустить программу еще раз и любой другой символ в противном случае')
        user_wants_to_continue = input()
        if user_wants_to_continue == '1':
            pass
        else:
            complete_flg = True

    print('Работа успешно завершена')
