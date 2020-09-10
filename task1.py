name = input("Введите ваше имя: ")
print("Привет,", name, end="!  ")
or_password = "123456"
password = input("Введите ваш пароль: ")
if password == or_password:
    print("Отлично. Вы ввели правильный пароль.")
else:
    print("Ошибка. Неправильный пароль")
