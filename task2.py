my_list = [17, 2, 5, 1, 8, 4, 3, 12]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {my_new_list}')

