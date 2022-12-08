from math import pi
from os import chdir
from random import randint as rnd
import sympy


# 1.Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.0001, π = 3.1415
# print(pi)
# # Вариант 1
# d = 0.001
# d = str(d)
# d = d[2:len(d)]
# d = len(d)
# print(round(pi, d))

# # Вариант с семинара
# def format(pi:float, d:float) -> float:
#     d = str(d)
#     d = len(d[d.find('.')+1::])
#     return float(f'{pi:0.{d}f}')
# d = 0.001
# print(format(pi, d))


# 2 и 3 задачи обьединила
# 2.Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 6 -> [2,3]
# 144 -> [2,3]
# n = 144
# list = []
# for i in range(2, n):
#     while n%i == 0:
#         list.append(i)
#         n//=i
# print(f'Cписок простых множителей: {list}')      

# # 3.Задайте последовательность чисел. Напишите программу, 
# # которая выведет список неповторяющихся элементов исходной последовательности.
# res = [] 
# for i in list:
#     if i not in res:
#         res.append(i)
# print(f'Список из неповторяющихся элементов: {res}')


# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. (записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

def write_file(stroka):
    chdir(r'C:\Users\Мария\Desktop\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar4')
    with open('file.txt', 'w') as f:
        f.write(stroka)

k = 2
stroka = ''
for i in range(k, -1, -1):
    stroka += f'{rnd(0,2)}x^{i}+'
    if i == 0:
        stroka += f'{rnd(0,100)}x^{i}'

print(stroka)
write_file(stroka)
    

# 5.Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt: 2*x**2 + 4*x + 5
# В file2.txt: 4*x**2 + 1*x + 4
# Результирующий файл: 6*x**2 + 5*x + 9
# chdir(r'C:\Users\Мария\Desktop\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar4')
# with open('file1.txt') as f:
#     a = f.read()
# print(a)

# with open('file2.txt') as f:
#     b = f.read()
# print(b)

# x = sympy.Symbol('x')
# c = sympy.simplify(a + '+' + b)
# c = str(c)
# print(c)

# with open('res.txt', 'w') as f:
#     f.write(c)

