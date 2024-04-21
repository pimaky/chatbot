import telebot
from random import randint
bot = telebot.TeleBot('7031668439:AAE46UQ3wNwQbhuepa0Hlnpgyz3H9PuvAhY')

@bot.message_handler(commands=['start'])
def start(message):
    global number
    number = randint(1, 100)
    global pmk
    pmk = 10
    bot.reply_to(message,'привет!\n'
                        'давай поиграем в числа!\n'
                        'я загадала число от 1 до 100, всего 10 попыток.\n'
                        'если число не будет отгадано, я буду говорить больше или меньше загаданное число.')

@bot.message_handler(func=lambda message: True)
def send_number(message):
    global pmk
    try:
        guess = int(message.text)
        if guess < number:
            bot.reply_to(message, 'не правильно! загаданное число больше.')
        elif guess > number:
            bot.reply_to(message, 'не правильно! загаданное число меньше.')
        else:
            bot.reply_to(message, 'правильно! вы угадали моё число, чтобы начать игру снова напишите /start')
            return
        pmk -= 1
        if pmk == 0:
            bot.reply_to(message, 'твои попытки закончились! загаданное число было: ' + str(pmk))
        else:
            bot.reply_to(message, 'попыток осталось: ' + str(pmk))
    except ValueError:
        bot.reply_to(message, 'введите число')
bot.polling(none_stop=True, interval=0)