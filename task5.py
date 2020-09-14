my_list = [3, 7, 5, 1, 9]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите новое число или 999 для выхода из программы: "))
while digit != 999:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Текущий рейтинг - {my_list}")
    digit = int(input("Введите следующее число: "))
