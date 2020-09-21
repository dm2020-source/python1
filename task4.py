my_list = [1, 5, 5, 2, 3, 2, 8, 10, 8, 7]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(f'Первый список чисел:  {my_list}')
print(f'Второй список чисел: {my_new_list}')

