import telebot
import random

bot = telebot.TeleBot('7028613085:AAH3vUno7cvDQcsywGIbpXLI8e-ZwWdrygg')

lives = 9
words = ['кошка', 'каток', 'олень', 'труба', 'время']
secret_word = ''
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False
game = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

@bot.message_handler(commands=['start'])
def start(message):
    global game, clue, secret_word
    game = True
    bot.send_message(message.chat.id,
                     "привет!! тебе нужно угадать слово по буквам или целиком")
    secret_word = random.choice(words)
    #print(secret_word)
    mess = ''
    for x in clue:
        mess += str(x) + ' '
    bot.send_message(message.from_user.id, mess)
    mess = 'осталось жизней: ' + heart_symbol * lives
    bot.send_message(message.from_user.id, mess)

@bot.message_handler(commands=['stopgame'])
def start(message, res=False):
    global game, clue, secret_word, lives
    game = False
    bot.send_message(message.chat.id,
                     "игра окончена!!\n"
                     "если хотите начать игру снова, напишите /start")
    secret_word = random.choice(words)
    print(secret_word)
    clue = list('?????')
    lives = 9

@bot.message_handler(commands=['stopgame'])
def start(message, res=False):
    global game, guessed_word_correctly, clue, secret_word, heart_symbol, lives
    guess = message.text

    if game:
        if lives > 0:
            if guess == secret_word or '' .join(clue) == secret_word:
                guessed_word_correctly = True
            if guess in secret_word:
                update_clue(guess, secret_word, clue)
                if '' .join(clue) == secret_word:
                    guessed_word_correctly = True
            else:
                bot.send_message(message.chat.id, "не правильно, ты потерял 1 жизнь!!")
                lives -= 1
            if guessed_word_correctly:
                bot.send_message(message.chat.id, "ура, ура, победа, победа, ура!! \n"
                                                  "слово было " + secret_word)
                lives = 9
                secret_word = random.choice(words)
                clue = list('?????')
                guessed_word_correctly = False
                game = False
                return

            mess = ''
            for x in clue:
                mess += str(x) + ' '
            bot.send_message(message.chat.id, mess)
            mess = 'осталось жизней ' + heart_symbol * lives
            bot.send_message(message.chat.id, mess)
        else:
            bot.send_message(message.chat.id, 'вы проиграли!!')
            game = False

    else:
        bot.send_message(message.chat.id, 'чтобы начать игру, напишите /start')


bot.polling(none_stop=True, interval=0)