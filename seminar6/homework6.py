# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# 3 любых задания(из любого урока)

def task1():
    """
    Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    Пример: для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
    """
    n = int(input('N: '))
    x = {x : 3*x + 1 for x in range(1, n+1)}
    print(x)

    f = '3*x+1'
    # n = int(input('N: '))
    x = {x: eval(f) for x in range(1, n+1)}
    print(x)

def task2():
    '''
    Дан список чисел. Создайте список, в который попадают числа, описываемые 
    возрастающую последовательность. Порядок элементов менять нельзя.
    Пример:
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    '''
    data = [1, 5, 2, 3, 4, 6, 1, 7]
    # Вариант 1
    li = []
    for i in range(len(data)):
        if data[i] == max(data[:i+1:]) and data[i] not in li:
                li.append(data[i])
    print(f'Вариант 1 -> {li}')
    # Вариант 2
    res = list(map(lambda x: data[x] == max(data[:x+1:]), range(len(data))))
    print(f'Вариант 2 -> {res}')
    
    # Вывод [1, 5, 6, 7]

def task3():
    '''
    Напишите программу, удаляющую из текста все слова, содержащие "абв".
    абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'
    '''
    text = 'абвгд гдежз жзе абв ыопыпт'
    li = list(filter(lambda x:'абв' not in x, text.split()))
    print(" ".join(li))


task2()
