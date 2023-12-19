# from temp2 import lst

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
# file.write(login + ':' + password)
# file.close()

def check(a, b):
    if ':' in a or ':' in b:
        return False
    if ':' not in a and ':' not in b:
        return True
    
def registr_pas():
    data_login = input('Введите логин: ') 
    data_password = input('Введите пароль: ') 
    if check(data_login, data_password) == True:
        with open('users.txt', 'a', encoding='utf-8') as file:
            file.writelines(data_login + ':')
            file.writelines(data_password + '\n')
            print('Вы зарегистрировались')
    if check(data_login, data_password) == False:
        print('Неверный логин или пароль')
registr_pas()