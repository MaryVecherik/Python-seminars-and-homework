# Урок 2. Знакомство с Python. Продолжение

# 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов
# Пример: для N = 5: 1, -3, 9, -27, 81
#геом прогрессия
# n = int(input('N: '))
# # решение 1
# x = 1
# for i in range(n):
#     print(x, end=' ')
#     x = x*-3

# # решение 2
# list = []
# for i in range(n):
#     list.append((-3)**i)
# print(list)

# 2.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input('N: '))
# x = {}
# for i in range(1, n+1):
#     x[i] = 3*i + 1   
# print(x)


# 3.Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# a = ('123123123')
# b = ('12')
# # решение 1
# count = 0
# for i in range(len(a)):
#     if a[i:i+len(b)] == b:
#         count += 1
# print(count)
# # решение 2
# print(a.count(b))

