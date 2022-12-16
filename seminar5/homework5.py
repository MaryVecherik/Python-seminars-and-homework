from random import randint as rnd


# На выбор:

# 1. Создайте программу для игры с конфетами.
# Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) человек против человека.
# b) добавьте игру против бота

def move_people(player, candies, max_move):
    """xод игрока"""
    valid = False
    while not valid:
        move = int(input(f'{player}, Ваш ход... '))
        if move > 0 and move <= max_move and move <= candies:
            print(f'Ты забрал(а) {move} конфет')
            candies -= move
            print(f'Осталось {candies} конфет')
            valid = True
        else:
            print(f'Количество взятых конфет должно быть до {max_move} или не больше оставшегося количества конфет')
    return candies

def move_bot(candies, max_move):
    """xод бота"""
    move = candies % (max_move + 1)
    if move == 0:
        move = rnd(1, max_move) if candies >= max_move else candies
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

def check_win(candies, set_move, player1, player2):
    """проверка выигрыша"""
    if candies == 0:
        return player1 if set_move % 2 == 0 else player2
    else:
        return False

def people():

    print('Привет! Тебя приветствует игра "Забери все конфеты!"')
    print('Основные правила игры: Дано 117 конфет, за один ход можно взять не более 28 конфет')
    print('Итак, начнём!')

    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    candies = 117 
    max_move = 28  

    count_for_check_win = candies // max_move
    set_move = rnd(1, 2) # 

    win = False
    while not win:
        if set_move % 2 == 0:
            candies = move_people(player1, candies, max_move)
        else:
            candies = move_people(player2, candies, max_move)
        
        if set_move >= count_for_check_win - 1:
            temp = check_win(candies, set_move, player1, player2)
            if temp:
                print(f'{temp} выиграл')
                win = True
        set_move += 1

def bot():
    print('Привет! Тебя приветствует игра "Забери все конфеты!"')
    print('Ты будешь играть с ботом.')
    print('Основные правила игры: Дано 117 конфет, за один ход можно взять не более 28 конфет')
    print('Итак, начнём!')

    player = input('Введите имя игрока: ')
    candies = 117 
    max_move = 28  

    count_for_check_win = candies // max_move #проверка выйгрыша
    set_move = rnd(1, 2) # установить ход

    win = False
    while not win:
        if set_move % 2 == 0:
            candies = move_people(player, candies, max_move)
        else:
            candies = move_bot(candies, max_move)

        if set_move >= count_for_check_win - 1:
            temp = check_win(candies, set_move, player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        set_move += 1


people()
# bot()



# 2.Создайте программу для игры в ""Крестики-нолики"".
#(в консоли происходит выбор позиции)