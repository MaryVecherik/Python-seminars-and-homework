# Урок 4. Данные, функции и модули в Python. Продолжение

def task1():
    """
    Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
    В качестве символа-разделителя используйте пробел.
    """
    # Вариант 1
    a = input().split()
    print(a)
    max = int(a[0])
    min = int(a[0])
    for i in range(len(a)):
        if int(a[i])>max:
            max = int(a[i])
        if int(a[i])<min:
            min = int(a[i])
    print(f'большее: {max}')
    print(f'меньшее: {min}')

    # Вариант 2
    n = input('Введите числа ').split()
    n = list((map(int, n)))
    print("Max = ", max(n), "Min = ", min(n))

def task2():
    """Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:"""
    a = -4
    b = -1
    c = 10
    print(f'{a}x² + {b}x + {c} = 0')

    # 1 - с помощью математических формул нахождения корней квадратного уравнения
    import math
    discr = b**2 - 4*a*c
    print(f'Дискриминант D = {discr}')
    if discr > 0: 
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(f'x1 = {round(x1,2)}, x2 = {round(x2,2)}')
    elif discr == 0:
        x = -b / (2*a)
        print(f'x = {round(x,2)}')
    elif discr < 0:
        print("Корней нет")

    # 2 - с помощью дополнительных библиотек Python
    import sympy
    x = sympy.Symbol('x')
    ans = sympy.solve(((a*x)**2) + (b*x) + c, x)
    print(ans)

def task3():
    """ 
    Задайте два числа. 
    Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
    """
    a = 4
    b = 8

    # Вариант 1
    res = 0
    if a > b:
        res = a
    else:
        res = b
    while(True): 
        if((res % a == 0) and (res % b == 0)): 
            res2 = res 
            break 
        res += 1
    print(f'Вариант 1 -> {res2}')

    # Вариант 2
    import math
    res = a*b
    print(f'Вариант 2 -> {res//math.gcd(a, b)}')

