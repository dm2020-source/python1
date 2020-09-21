def sal():
    try:
        time = float(input('Введите количество отработанных часов: '))
        salary = int(input('Введите ставку за час: '))
        bonus = int(input('Введите премию: '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника:  {res}')
    except ValueError:
        return print('Ошибка, введеное значение не цифровое.')
sal()



