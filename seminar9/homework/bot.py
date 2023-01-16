import telebot
from cfg import TOKEN
from random import randint as rnd

bot = telebot.TeleBot(TOKEN)
candys = dict() 
move = dict()

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print(message)
    global candys, move
    move[message.chat.id] = rnd(1, 2)
    candys[message.chat.id] = 117
    max_take = 28
    player = message.chat.first_name
    bot.send_message(message.chat.id, f'Привет {player}! Тебя приветствует игра "Забери все конфеты!"')
    bot.send_message(message.chat.id, f'Основные правила игры: Дано {candys[message.chat.id]} конфет, за один ход можно взять не более {max_take} конфет')
    
    while True:
                if move[message.chat.id] % 2 == 0:
                    msg = bot.send_message(message.chat.id, f'{player}, Ваш ход... ') #ходит человек
                    print(message)
                    candys[message.chat.id] = bot.register_next_step_handler(msg, take_people)
                else:
                    take = rnd(1, candys[message.chat.id] % (max_take + 1)) #ходит бот
                    bot.send_message(message.chat.id, f'Бот забрал {take} конфет')
                    candys[message.chat.id] -= take
                    bot.send_message(message.chat.id, f'Осталось {candys[message.chat.id]} конфет')

                # if move[message.chat.id] >= (candys[message.chat.id] // max_take) - 1:
                #     temp = win()
                #     if temp:
                #         bot.send_message(message.chat.id, f'{temp} выиграл')
                
                if move[message.chat.id] >= (candys[message.chat.id] // max_take) - 1:
                    if candys[message.chat.id] <= 28:
                        if move % 2 == 1:
                            bot.send_message(message.chat.id, f'{player} выиграл')
                        else:
                            bot.send_message(message.chat.id, 'Bыиграл Бот')
                            break
                
                move[message.chat.id] += 1


def take_people(message):
    """Ход человека"""
    global max_take, candys
    while True:
            # take = int(message.text)
            if int(message.text) > 0 and int(message.text) <= max_take and int(message.text) <= candys[message.chat.id]:
                bot.send_message(message.chat.id, f'Ты забрал(а) {int(message.text)} конфет')
                candys[message.chat.id] -= int(message.text)
                bot.send_message(message.chat.id, f'Осталось {candys[message.chat.id]} конфет')
                break
            else:
                bot.send_message(message.chat.id, f'Столько взять нельзя. Можно взять до {28} или не больше оставшегося количества конфет')
            
            return candys[message.chat.id]


def win(message):
    """Чей выйгрыш"""
    global player, candys, move
    if candys[message.chat.id] <= 28:
        return player if move % 2 == 1 else 'Бот'
    else:
        return False


print('server start')
bot.infinity_polling()
