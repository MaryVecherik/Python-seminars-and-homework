from os import chdir

def add_data(data):
    """ Добавление контакта """
    chdir(r'C:\Users\Мария\OneDrive\Рабочий стол\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar7\homework')
    with open('base.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{data}')
        print('Контакт добавлен')

def get_data():
    """ Получить """
    chdir(r'C:\Users\Мария\OneDrive\Рабочий стол\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar7\homework')
    with open('base.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        return data