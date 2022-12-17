import math
import os
import random

def task1():
    """
    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    Пример:
    6782 -> 23
    0,56 -> 11
    """
    num = input('Введите число: ') 
    sum = 0
    for i in num:
        if i!='.' and i!=',' and i!='-':
            sum += int(i)
    print(f'Сумма числа = {sum}')

def task2():
    """
    Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    Пример:
    пусть N = 4, тогда [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)
    """
    n = int(input('N: '))
    res = 1
    for i in range(1, n+1):
        res *= i
        print(res, end=' ')

def task3():
    """
    Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
    Пример:
    Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
    """
    n = int(input('N: '))
    res = 1
    sum = 0
    for i in range(1, n+1):
        res= math.pow((1+1/i), i)
        sum += i
        print(res, end=' ')
    print('\n' + f'Сумма элементов = {sum}')

def task4():
    """
    Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    Найдите произведение элементов на указанных позициях. 
    Позиции хранятся в файле file.txt в одной строке одно число.
    (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 
    Позиции: 0,1 -> 2
    """
    os.chdir(r'C:\Users\Мария\Desktop\Учеба\2 четверть\1. Знакомство с Python\Семинары и домашка\Python\seminar2')
    with open('file.txt') as f:
        a = f.read().split('\n')
    print(a)
    f.close()

    n = int(input('Количество элементов: N = '))
    list = []
    for i in range(-n, n+1):
            list.append(i)
    print(list)

    pr = 1
    for i in a:
        pr *= list[int(i)]        
    print(pr)

def task5():
    """Реализуйте алгоритм перемешивания списка."""
    list = []
    for i in range(5):
        list.append(i)
    print("Исходный список: ")
    print(list)
    print("Перемешанный список: ")
    random.shuffle(list)   
    print(list)

task4()