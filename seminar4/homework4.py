from math import pi
from os import chdir
from random import randint as rnd
import sympy

def task1():
    """
    1.Вычислить число Пи c заданной точностью d
    Пример:
    при d = 0.001, π = 3.141
    при d = 0.0001, π = 3.1415
    """
    d = str(input('Введите точность в формате "0.001": '))
    d = d[2:len(d)]
    d = len(d)
    print(round(pi, d))

    # Вариант с семинара
    def format_by_mask(num: float, d: float) -> float:
        """Форматирует число в заданной маске"""
        d = str(d)
        d = len(d[d.find('.')+1::])
        return float(f'{pi:0.{d}f}') #f'a:0.3f'

    d = input('Введите точность в формате "0.001": ')
    print(f'Вариант с семинара -> {format_by_mask(pi, d)}')

# 2 и 3 задачи обьединила
def task2_and_task3():
    """
    2.Задайте натуральное число N. Напишите программу, 
    которая составит список простых множителей числа N.
    6 -> [2,3]
    144 -> [2,3]
    """
    n = 144
    list = []
    for i in range(2, n):
        while n%i == 0:
            list.append(i)
            n//=i
    print(f'Cписок простых множителей: {list}')

    """
    3.Задайте последовательность чисел. Напишите программу, 
    которая выведет список неповторяющихся элементов исходной последовательности.
    """
    res = [] 
    for i in list:
        if i not in res:
            res.append(i)
    print(f'Список из неповторяющихся элементов: {res}')

# Задача 2 с семинара
def task2_seminar():
    def dividers(a: int, uniq: bool = False) -> list[int]:
        """"Возвращает список простых делителей числа.
        uniq = True вернет список уникальных делителей"""
        i = 2
        dividers = []
        while a != 1:
            while a % i == 0:
                dividers.append(i)
                a //= i
            i += 1
        if uniq:
            return list(set(dividers))
        else:
            return dividers

    a = 144
    print(f'Список натуральных делителей числа {a}:{dividers(a)}')
    print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')

# Задача 3 с семинара
def task3_seminar():
    mass = [rnd(1,7) for i in range(12)]
    print(f'Исходный список: {mass}')
    print(f'Список уникальных элементов: {list(set(mass))}')
    mass = [i for i in mass if mass.count(i)==1]
    print(f'Uniq: {mass}')

def task4():
    """
    4. Задана натуральная степень k. 
    Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
    и записать в файл многочлен степени k. (записать в строку)
    Пример:
    k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
    k=3 => 2*x^3 + 4*x^2 + 4*x + 5
    """
    def write_file(stroka: str):
        """"Записывет в фаил наш полином"""
        chdir(r'C:\Users\Мария\Desktop\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar4')
        with open('file.txt', 'w') as f:
            f.write(stroka)
            f.close()

    def create_stroka(k: int) -> str:
        """"Генерирует полином со случайными коэффициентами степени k
        simple = False вернет полином без сокращения 0 коэффициентов"""
        stroka = ''
        for i in range(k, -1, -1):
            stroka += f'{rnd(0,2)}x^{i}+'
            if i == 0:
                stroka += f'{rnd(0,100)}'
        return str(stroka)
        
    k = 4
    stroka = create_stroka(k)
    print(stroka)
    write_file(stroka)
    
def task5():
    """
    5.Даны два файла, в каждом из которых находится запись многочлена. 
    Задача - сформировать файл, содержащий сумму многочленов.
    В file1.txt: 2*x**2 + 4*x + 5
    В file2.txt: 4*x**2 + 1*x + 4
    Результирующий файл: 6*x**2 + 5*x + 9
    """
    chdir(r'C:\Users\Мария\Desktop\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar4')
    with open('file1.txt') as f:
        a = f.read()
        f.close()
    print(a)
    

    with open('file2.txt') as f:
        b = f.read()
        f.close()
    print(b)

    x = sympy.Symbol('x')
    c = sympy.simplify(a + '+' + b)
    c = str(c)
    print(c)

    with open('res.txt', 'w') as f:
        f.write(c)
        f.close()

task5()