from datetime import datetime

def log_in(data):# функция для фиксации входа в систему
    time = datetime.now().strftime('%c')
    with open('logger.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{time} Пользователь {data} вошел в систему.\n')
        

def log_sing_up(data):# фиксация регистрации пользователя
    time = datetime.now().strftime('%c')
    with open('logger.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{time} Пользователь {data} был успешно зарегистрирован в системе. \n')
        
def log_out(data):# функция для фиксации выхода из системы
    time = datetime.now().strftime('%c')
    with open('logger.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{time} Пользователь {data} вышел из системы.\n')

def uncorrect_password(data):# функция для фиксации попытки входа в систему
    time = datetime.now().strftime('%c')
    with open('logger.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{time} была попытка входа в систему. Неправильно ввели пароль. {data} пытался войти в систему. \n')
        
def add_data(data,user):# функция указывает,что были добавлены изменения в базу
    time = datetime.now().strftime('%c')
    with open('logger.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{time} Пользователем {user} была добавнена информация: {data} \n')
        
def exp_data(data,user):# функция указывает,что был поиск по словам
    time = datetime.now().strftime('%c')
    with open('logger.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{time} Пользователь {user} делал запрос следующего слова: {data} \n')