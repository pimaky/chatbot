import telebot

bot = telebot.TeleBot('6859553632:AAF0x3kn9EJqB2havx5zSHw7_NwFckcPHCU')

words = ['яблоко - apple'
         'птица - bird'
         'чай - tea'
         'автобус - bus'
         'кофе - coffee'
         'кухня - kitchen'
         'на полпути - halfway'
         'тихий - silent'
         'лебедь - swan'
         'кот - cat'
         'пчела - bee'
         'желание - wish'
         ' - ']

@bot.message_handler(commands=['start'])
def start(message, res=False):
    bot.send_message(message.chat.id, "привет!! я могу помочь тебе изучить английские слова \n"
                                      "чтобы узнать новые слова, введи /word \n"
                                      "чтобы проверить твои знания с помощью теста, введи \n")

@bot.message_handler(commands=['word'])
def word(message):


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "что-что??")