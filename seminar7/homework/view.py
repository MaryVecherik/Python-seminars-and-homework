import model

def choose_mode():
    """ Выбор режима прогроммы """
    return (input('Введите режим программы(1-добавление, 2-поиск): '))


def new_data():
    """ Новый контакт """
    last_name = input('Введите Фамилию: ')
    phone = input('Введите Телефон: ')
    return (f'{last_name} // {phone}')


def search_data():
    """ Данные для поиска """
    data = (input('Введите данные для поиска: '))
    return data


def show_data(data):
    """ Показать """
    print('Результат поиска: ')
    for i in data:
        print(i)