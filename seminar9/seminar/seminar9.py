
import telebot
from cfg import TOKEN

def task_bot():
    """
    Напишите программу, удаляющую из сообщения, которое прислал пользователь все слова, 
    содержащие "абв" и отправляет его обратно пользователю.
    Сообщение пользователя: абв гдеабв тофыптфыптфып
    Ответ бота: тофыптфыптфып
    """
    
    def del_abv(message):
        li = list(filter(lambda x:'абв' not in x, message.split()))
        return " ".join(li)

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.send_message(message.chat.id, del_abv(message.text))
        bot.send_message(message.chat.id, f'из исходной строки {message.text} удалены все слова с "абв"')

    print('server start')

    bot.infinity_polling()


task_bot()
