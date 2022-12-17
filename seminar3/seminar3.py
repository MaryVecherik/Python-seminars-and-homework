# Урок 3. Данные, функции и модули в Python

def task1():
    """Задайте список. 
    Напишите программу, которая определит, присутствует ли в заданном списке некое число.
    """
    # Вариант 1
    list = ['a', 'asd', '8974']
    tmp = len(list)
    for i in list:
        if type(i) == int or type(i) == float:
            tmp = tmp - 1
    if tmp < len(list):
        print ("Yes")
    else:
        print ("No")

    # Вариант 2
    mass = ['ssss', 'sngujn556', 44]
    types = [str(type(i)) for i in mass]
    if "<class 'int'>" in types or "<class 'float'>" in types:
        print('Yes')
    else:
        print('No')

def task2():
    """
    Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
    Пример:
    список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
    список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
    список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
    список: ["123", "234", 123, "567"], ищем: "123", ответ: 2
    список: [], ищем: "123", ответ: -1
    """
    # Вариант 1
    list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    str = "qwe"
    count = 0
    index = 0
    for i in list:
        if i == str:
            count += 1
            if count == 2:
                print(index)
                break
        index += 1
    if count < 2:
        print("-1")

    # Вариант 2
    mass = ["йцу", "фыв", "ячс", "цук", "йцукен"]
    a = "йцу"
    try:
        mass.remove(a)
        print((mass.index(a))+1)
    except ValueError:
        print(-1)

    # Вариант 3
    mass1 = ["123", "234", "123", "567"]
    a = "123"

    if mass1.count(a) < 2:
        print(-1)
    else:
        mass1.remove(a)
        print((mass1.index(a))+1)

task2()