from config import BOT_TOKEN 
from telebot import TeleBot
from anekdot import get_new_anekdot

bot = TeleBot(token=BOT_TOKEN)

help_message = """
/anekdot - вывод случайного анекдота
"""

@bot.message_handler(commands=['help'])
def send_help(message):
    #bot.send_message(message.chat.id, text=help_message )
    pass

def send_random_anekdot(message):
    anekdot = get_new_anekdot()
    bot.send_message(message.chat.id, text=anekdot)
    bot.send_message(message.chat.id, text="ещё один анекдот? /anekdot")
bot.message_handler(commands=['anekdot'])(send_random_anekdot)

@bot.message_handler(func=lambda m: True)
def unknown_command(message):
 known_commands = ['/anekdot', '/help']
 if message.text.split()[0] not in known_commands:
     #bot.reply_to(message, "Некорректный ввод. Введите /help для просмотра доступных функций")
     pass
 
bot.polling()

