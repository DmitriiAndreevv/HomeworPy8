from import_students import import_students
from export_students import export_students
from print_data import print_data
from search_students import search_students
from log import *



def function_pb():
    print( 'База данных студентов учащихся в вузе \n\
            Для регистрации студента нажмите 1: \n\
            Для входа в личный кабинет нажмите 2: \n\
            Если возникла ошибка,повторите попытку. ')

    data = input('Введите номер: ')
    if data == '1':
        return reg_user()
    elif data == '2':
        return user_log_in()
    else:
        print('Неверная команда ввода,введите указанные номера: \n')
        return function_pb()

def input_data(user):
    First_name = input ('Введите имя: ')
    Second_name = input('Введите фамилию: ')
    Middle_name = input('Введите отчество: ')
    birthday = input('Дата рождения: ')
    number_phone = input('Номер телефона: ')
    list1 = [First_name, Second_name, Middle_name, birthday, number_phone]
    return list1,user
    

def function_todo(user):
    print('Введите команду: \n\
    1 - импорт: \n\
    2 - экспорт: \n\
    3 - поиск контакта: \n\
    4 - закончить работу с программой.')
    choise = input('Введите команду : ')
    if choise == '1':
        sep = None
        import_students(input_data(user), sep)
        print()
        function_todo(user)
    elif choise == '2':
        data = export_students()
        print_data(data)
        print()
        function_todo(user)
    elif choise == '3':
        search = input('Введите данные для поиска: ')
        data = export_students()
        item = search_students(search, data)
        export_students(search, user)
        if item != None:
            print('Фамилия'.center(20),'Имя'.center(20),'Отчество'.center(20),'Дата рождения'.center(20),'Телефон'.center(15))
            print('-'*130)
            print(item[0].center(20),item[1].center(20),item[2].center(20),item[3].center(20),item[4].center(15))
            print()
            function_todo(user)
        else:
            print('Данные не обнаружены')
            print()
            function_todo(user)
    elif choise == '4':
        log_out(user)
        return print('Вы вышли из программы! \n')
    else:
        print('Неверно введены данные.')
        return function_todo(user)
            

           

def reg_user():
    user = input('Введите имя пользователя: ')
    with open ('users.txt', 'a+', encoding='utf-8') as regist:
        regist.write('\n')
    check_name('users.txt',user)
    reg_password()
    function_pb()


def reg_password():
    password = input('Введите пароль: ')
    check_pass = (input('Введите пароль ещё раз: '))
    if password == check_pass:
        with open ('users.txt', 'a', encoding='utf = 8') as pasw:
            pasw.write('\n')
            pasw.write(f'{password}')
            print('Welcome to our studying!')
            print()
    else:
        print('Неверный пароль.')
        print()
        return reg_password()


def check_name(file,usr):
    with open(file,'r',encoding='utf-8') as f:
        a = True
        while a:
            file_line = f.read()
            if usr in file_line:
                return check_name(file,input('Пользователь с таким именем уже зарегистрирован.\n\
                                         Введите другое имя: '))
            a = False
        else:
            with open(file,'a',encoding='utf-8') as us:
                    us.write('\n')
                    us.write(f'{usr}')
                    log_sing_up(usr)
                    a=False
                    


def user_log_in():
    user=input('Enter user name: ')
    with open('users.txt','r',encoding='utf-8') as us:
        a = True
        while a:
            file_line = us.readline()
            if user in file_line:
                log_pass(user)
                a = False
            elif not file_line:
                print('Пользователь не найден.Повторите попытку.')
                return user_log_in()
            a = False
    function_todo(user)

def control_pass(list,user,pas):
    list_new=[]
    for i in list:
        i=i.replace('\n','')
        list_new.append(i)
    for i in list_new:
        if i == user:
            index=list_new.index(user)
            if pas == list_new[index+1]:
                return
            else:
                print("Invalid password.")

                return log_pass(user)

def log_pass(user):
    pas=input('Enter password: ')
    with open('users.txt','r+',encoding='utf-8') as us:
        file_line = us.readlines()
        some_list=[]
        for file in file_line:
            if file=='\n':
                continue
            else:
                some_list.append(file)
    control_pass(some_list,user,pas)