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

def auth():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    with open('users.txt', 'r', encoding='utf-8') as file:
        for i in file.readlines():
            reg_login, reg_password = i.strip().split(':')
            if reg_login == login and reg_password == password:
                print('Доступ разрешен')
                return
        print('Логин или пароль неверны. Перейдите к регистрации.')
auth()


def check():
    lst = []
    with open('users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            login, password = line.strip().split(":")
            lst.append((login, password))
    new_list = [item for sublist in lst for item in sublist]
    print(new_list)
check()
