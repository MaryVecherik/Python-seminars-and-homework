from os import chdir
import csv

def add_data(data):
    """ Добавление контакта """
    chdir(r'C:\Users\Мария\OneDrive\Рабочий стол\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar7\homework')
    with open('base.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{data}')
        f.close()

    with open('base.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter = ";", lineterminator="\n")
        writer.writerows([data.split(' // ')])
        f.close()

    print('Контакт добавлен')


def get_data_txt():
    """ Получить """
    chdir(r'C:\Users\Мария\OneDrive\Рабочий стол\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar7\homework')
    with open('base.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        f.close()
        return data

def get_data_csv():      # доделать  
    with open('base.csv', 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        for row in data:
            print(row)


    
