# with open('user.txt', 'w', encoding='utf-8') as file:
#     file.write('login:password')
# with open('user.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#     login, password = data.split(':')
#     login = data[0]
#     password = data[1]

# file = open('user.txt', 'a', encoding='utf-8')
# login = input('Введите логин: ')
# password = input('Введите пароль: ')
# file.write(login +':'+password)
# file.close()
# with open('user.txt', 'a', encoding='utf-8') as file:
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     file.write(login +':'+password+'\n')


def menu():
    while True:
        pr = input('''Добро пожаловать! Выберите пункт меню:
        1. Регистрация
        2. Авторизация
        3. Выход\n''')
        if pr == '1':
            print('Зарегистрируйтесь')
            registr_pas()
        elif pr == '2':
            print('Авторизуйтесь')
            if auth():
                break
        elif pr == '3':
            print('Завершение работы')
            break
        else:
            print('Некорректный ввод. Пожалуйста, выберите пункт меню.')

def auth():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    with open('users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            reg_login, reg_password = line.strip().split(':')
            if reg_login == login and reg_password == password:
                print('Доступ разрешен')
                return True
        print('Логин или пароль неверны. Перейдите к регистрации.')
        return False

def check():
    lst = []
    with open('users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            login, password = line.strip().split(":") if ":" in line else (None, None)
            lst.append((login, password))
    new_list = [item for sublist in lst for item in sublist]
    return new_list

def check1(a, b):
    if ':' in a or ':' in b:
        return False
    if ':' not in a and ':' not in b:
        return True

def registr_pas():
    data_login = input('Введите логин: ')
    data_password = input('Введите пароль: ')
    if check1(data_login, data_password) and data_login not in check():
        with open('users.txt', 'a', encoding='utf-8') as file:
            file.write(data_login + ':' + data_password + '\n')
        print('Вы зарегистрировались')
    else:
        print('Некорректный логин или пароль')

menu()
