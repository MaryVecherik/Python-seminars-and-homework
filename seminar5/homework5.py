from random import randint as rnd

# На выбор:

def task1():
    """
    1. Создайте программу для игры с конфетами.
    Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
    Все конфеты оппонента достаются сделавшему последний ход.
    a) человек против человека.
    b) добавьте игру против бота
    """
    def move_people(player, candies, max_take):
        """xод игрока"""
        while True:
            move = int(input(f'{player}, Ваш ход... '))
            if move > 0 and move <= max_take and move <= candies:
                print(f'Ты забрал(а) {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                break
            else:
                print(f'Количество взятых конфет должно быть до {max_take} или не больше оставшегося количества конфет')
        return candies

    def move_bot(candies, max_take):
        """xод бота"""
        move = candies % (max_take + 1)
        if move == 0:
            move = rnd(1, max_take) if candies >= max_take else candies
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

    def people(candies, max_take):
        print('Итак, начнём!')
        player1 = input('Введите имя первого игрока: ')
        player2 = input('Введите имя второго игрока: ')
        
        count_for_check_win = candies // max_take
        set_move = rnd(1, 2) # 

        while True:
            if set_move % 2 == 0:
                candies = move_people(player1, candies,max_take)
            else:
                candies = move_people(player2, candies, max_take)
            
            if set_move >= count_for_check_win - 1:
                temp = check_win(candies, set_move, player1, player2)
                if temp:
                    print(f'{temp} выиграл')
                    break
            set_move += 1

    def bot(candies, max_take):
        print('Ты будешь играть с ботом.')
        print('Итак, начнём!')
        player = input('Введите имя игрока: ')
        
        count_for_check_win = candies // max_take #проверка выйгрыша
        set_move = rnd(1, 2) # установить ход

        while True:
            if set_move % 2 == 0:
                candies = move_people(player, candies, max_take)
            else:
                candies = move_bot(candies, max_take)

            if set_move >= count_for_check_win - 1:
                temp = check_win(candies, set_move, player, 'Бот')
                if temp:
                    print(f'{temp} выиграл')
                    break
            set_move += 1

    print('Привет! Тебя приветствует игра "Забери все конфеты!"')
    print('Основные правила игры: Дано 117 конфет, за один ход можно взять не более 28 конфет')
    candies = 117 
    max_take = 28 
        
    people(candies, max_take)
    bot(candies, max_take)

def task2():
    """
    2.Создайте программу для игры в ""Крестики-нолики"".
    (в консоли происходит выбор позиции)
    """
    print('Привет! Тебя приветствует игра "Крестики-нолики!"')





