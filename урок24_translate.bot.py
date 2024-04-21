import telebot
from googletrans import Translator
import gtts
import os

bot = '7140030646:AAEQjCgdHbGtLehcz30m0svcEZve4tW-Lu8'
translator = Translator()
dest_lang = 'en'

languages = {
             'russian': 'ru',
             'english': 'en',
             'french': 'fr',
             'italian': 'it',
             'spanish': 'es',
             'kazach': 'kz',
             'china': 'zh-CN',
             'korean': 'ko',
             'latin': 'la',
             'german': 'de'
}

def translateText(text):
    global dest_lang
    translated = translator.translate(text, dest=dest_lang)
    translated = translated.text
    return translated

def voice(text):
    global dest_lang
    audiofile = text +'.mp3'
    voice = gtts.gTTS(text, lang=dest_lang, slow=True)
    voice.save(audiofile)
    return audiofile

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'привет!! я бот-переводчик.\n'
                          'для перевода введи /translate \n'
                          'для смены языка введи /changelang')

@bot.message_handler(commands=['translate'])
def translate(message):
    text = message.text
    text = text.replace('/translate', '').strip()
    translated = translateText(text)
    bot.reply_to(message, translated)

    audiofile = voice(translated)
    f = open(audiofile, 'rb')
    bot.send_message(message.chat.id, f)
    f.close()
    os.remove(audiofile)

@bot.message_handler(commands=['changelang'])
def changelang(message):
    global dest_lang, languages
    language = message.text
    language = language.replace('/changelang', '').strip()
    language = language.lower()
    dest_lang = languages[language]
    bot.send_message(message.chat.id, 'вы установили ' +language+ ' язык')

@bot.message_handler(commands=['help'])
def help(message):
    global languages, dest_lang
    msg = 'я могу перервести любой текст на следующие языки: \n'
    for key in languages.keys():
        msg += key
        msg +='\n'
    msg += 'для смены языка введите команду /changelang'
    bot.send_message(message.chat.id, msg)
    msg = 'сейчас установлен '
    for key, value in languages.items():
        if dest_lang == value:
            msg += key
    bot.send_message(message.chat.id, msg)
bot.polling(none_stop=True)