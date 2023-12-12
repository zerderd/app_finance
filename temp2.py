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
with open('user.txt', 'a', encoding='utf-8') as file:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    file.write(login +':'+password+'\n')

