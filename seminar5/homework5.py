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
    def move_people(player, candys, max_take):
        """Ход человека"""
        while True:
            move = int(input(f'{player}, Ваш ход... '))
            if move > 0 and move <= max_take and move <= candys:
                print(f'Ты забрал(а) {move} конфет')
                candys -= move
                print(f'Осталось {candys} конфет')
                break
            else:
                print(f'Столько взять нельзя. Можно взять до {max_take} или не больше оставшегося количества конфет')
        return candys

    def move_bot(candys, max_take):
        """Ход бота"""
        move = candys % (max_take + 1)
        if move == 0:
            move = rnd(1, max_take) if candys >= max_take else candys
        print(f'Бот забрал {move} конфет')
        candys -= move
        print(f'Осталось {candys} конфет')
        return candys

    def win(candys, move, player1, player2):
        """Чей выйгрыш"""
        if candys == 0:
            return player1 if move % 2 == 0 else player2
        else:
            return False

    def people(candys, max_take):
        """Игра с человеком"""
        print('Итак, начнём!')
        player1 = input('Введите имя первого игрока: ')
        player2 = input('Введите имя второго игрока: ')
        
        move = rnd(1, 2)
    
        while True:
            if move % 2 == 0:
                candys = move_people(player1, candys, max_take)
            else:
                candys = move_people(player2, candys, max_take)
            
            if move >= (candys // max_take) - 1:
                temp = win(candys, move, player1, player2)
                if temp:
                    print(f'{temp} выиграл')
                    break
            move += 1

    def bot(candys, max_take):
        """Игра с ботом"""
        print('Ты будешь играть с ботом.')
        print('Итак, начнём!')
        player = input('Введите имя игрока: ')
        
        move = rnd(1, 2) 

        while True:
            if move % 2 == 0:
                candys = move_people(player, candys, max_take)
            else:
                candys = move_bot(candys, max_take)

            if move >= (candys // max_take) - 1:
                temp = win(candys, move, player, 'Бот')
                if temp:
                    print(f'{temp} выиграл')
                    break
            move += 1


    candys = 117 
    max_take = 28 
    print('Привет! Тебя приветствует игра "Забери все конфеты!"')
    print(f'Основные правила игры: Дано {candys} конфет, за один ход можно взять не более {max_take} конфет')
    print('С кем хочешь играть? Введи 1 - человек, 2 - бот: ')
    game = int(input()) 
    if game == 1:
        people(candys, max_take) 
    else:
        bot(candys, max_take)





def task2():
    """
    2.Создайте программу для игры в ""Крестики-нолики"".
    (в консоли происходит выбор позиции)
    """
    print('Привет! Тебя приветствует игра "Крестики-нолики!"')


task1()

