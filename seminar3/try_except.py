# Пример try except 
# Проверка на ввод числа
def input_correct_int():
    while True:
        try:
            return int(input())
            break
        except:
            print('Некорректный ввод')

a = input_correct_int()
print(a)
