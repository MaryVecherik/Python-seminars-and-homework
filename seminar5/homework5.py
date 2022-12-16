from random import randint as rnd


# На выбор:
# 1. Создайте программу для игры с конфетами.
# Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) человек против человека.
# b) добавьте игру против бота

def move_player(player, candies, max_move):
    """Ход игрока"""
    valid = False
    while not valid:
        move = int(input(f'{player}, Ваш ход... '))
        if move > 0 and move <= max_move and move <= candies:
            print(f'Вы забрали {move} конфет')
            candies -= move
            print(f'Осталось {candies} конфет')
            valid = True
        else:
            print(f'Количество взятых конфет должно быть от 1 до {max_move} или не больше оставшегося количества конфет')
    return candies

def check_win(candies, determing_moves, player1, player2):
    """ """
    if candies == 0:
        return player1 if determing_moves % 2 == 0 else player2
    else:
        return False


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
candies = 117 
max_move = 28  



count_for_check_win = candies // max_move
determing_moves = rnd(0, 1) # определить ход

win = False
while not win:
    if determing_moves % 2 == 0:
        candies = move_player(player1, candies, max_move)
    else:
        candies = move_player(player2, candies, max_move)
    
    if determing_moves >= count_for_check_win - 1:
        temp = check_win(candies, determing_moves, player1, player2)
        if temp:
            print(f'{temp} выиграл(а)')
            win = True
    determing_moves += 1

    
    


# OST(m+1)K
# m = 28
# K = 117





# 2.Создайте программу для игры в ""Крестики-нолики"".
#(в консоли происходит выбор позиции)