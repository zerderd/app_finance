data_login = input('Введите логин: ') 
data_password = input('Введите пароль: ')
with open('users.txt', 'a', encoding='utf-8') as file:
    file.writelines(data_login + ' ')
    file.writelines(data_password + '\n')
