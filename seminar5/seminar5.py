# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

def task1():
    """
    Задано N натуральных чисел, записанных через пробел.
    Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
    Найдите это число.
    1 2 3 4 6 7 -> 5
    1 3 -> 2
    3 4 6 7 8 -> 5 
    """
    stroka = '1 2 3 4 6 7'
    data = list(map(int, stroka.split()))
    print(data)
    li = []
    for i in range(1, len(data)):
        if data[i]-1 != data[i-1]: 
            li.append(data[i]-1)
    print(li)

def task2():
    '''
    Дан список чисел. Создайте список, в который попадают числа, описываемые 
    возрастающую последовательность. Порядок элементов менять нельзя.
    Пример:
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    '''
    data = [1, 5, 2, 3, 4, 6, 1, 7]
    # Вариант 1
    a = [data[0]]
    for i in data:
        if i > max(a):
            a.append(i)
    print(f'Вариант 1 -> {a}')
    # Вариант 2
    li = []
    for i in range(len(data)):
        if data[i] == max(data[:i+1:]) and data[i] not in li:
                li.append(data[i])
    print(f'Вариант 2 -> {li}')

def task3():
    '''
    Напишите программу, удаляющую из текста все слова, содержащие "абв".
    абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'
    '''
    # Вариант мой
    text = 'абвгд гдежз жзе абв ыопыпт'
    li = list(filter(lambda x:'абв' not in x, text.split()))
    print(" ".join(li))

    # Вариант преподавателя
    del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])
    print(del_st('абвгд гдежз жзе абв ыопыпт', 'абв'))

task2()