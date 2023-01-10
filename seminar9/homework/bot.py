import telebot
from cfg import TOKEN
from random import randint as rnd

bot = telebot.TeleBot(TOKEN)
candys = dict() 
move = dict() 

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    global candys, move
    move[message.chat.id] = rnd(1, 2)
    candys[message.chat.id] = 117
    max_take = 28
    player = message.chat.username
    bot.send_message(message.chat.id, f'Привет{message.chat.username}! Тебя приветствует игра "Забери все конфеты!"')
    bot.send_message(message.chat.id, f'Основные правила игры: Дано {candys[message.chat.id]} конфет, за один ход можно взять не более {max_take} конфет')
    
    while True:
            if move[message.chat.id] % 2 == 0:
                candys[message.chat.id] = move_people(player, candys[message.chat.id], max_take)
            else:
                candys[message.chat.id] = move_bot(candys[message.chat.id], max_take)

            if move[message.chat.id] >= (candys[message.chat.id] // max_take) - 1:
                temp = win(candys[message.chat.id], move[message.chat.id], 'Бот')
                if temp:
                    print(f'{temp} выиграл')
                    break
            move[message.chat.id] += 1


@bot.message_handler()
def move_people(message):
    """Ход человека"""
    global player, max_take
    while True:
        move = bot.send_message(message.chat.id, f'{player}, Ваш ход... ')
        if move > 0 and move <= max_take and move <= candys[message.chat.id]:
            bot.send_message(message.chat.id, f'Ты забрал(а) {move} конфет')
            candys[message.chat.id] -= move
            bot.send_message(message.chat.id, f'Осталось {candys[message.chat.id]} конфет')
            break
        else:
            bot.send_message(message.chat.id, f'Столько взять нельзя. Можно взять до {max_take} или не больше оставшегося количества конфет')
        return candys[message.chat.id]

@bot.message_handler()
def move_bot(message):
    """Ход бота"""
    global player, max_take
    move = candys[message.chat.id] % (max_take + 1)
    if move == 0:
        move = rnd(1, max_take) if candys[message.chat.id] >= max_take else candys[message.chat.id]
        bot.send_message(message.chat.id, f'Бот забрал {move} конфет')
        candys[message.chat.id] -= move
        bot.send_message(message.chat.id, f'Осталось {candys[message.chat.id]} конфет')
        return candys[message.chat.id]

@bot.message_handler()
def win(message):
    """Чей выйгрыш"""
    global player
    if candys[message.chat.id] <= 28:
        return player if move % 2 == 1 else 'Бот'
    else:
        return False




print('server start')

bot.infinity_polling()