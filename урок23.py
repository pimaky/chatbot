import telebot
from pydub import AudioSegment
import speech_recognition as sr
import os
import pyttsx3

token = '7040380043:AAFS6S56kTtJa0WwK6WqIaO0yxCFtaPlXdU'
bot = telebot.TeleBot(token)
tts = pyttsx3.init()
voices = tts.getProperty('voices')
for voice in voices:
    print('======')
    print('имя: %s' % voice.name)
    print('ID: %s' % voice.id)

@bot.message_handler(context_types=['text'])
def get_text_message(message):
    bot.reply_to(message, 'перевариваю сообщение')
    text = message.text
    speech = TextToSpeech(text)
    f = open(speech, 'rb')
    bot.send_voice(message.chat.id, f)
    f.close()
    os.remove(speech)

def TextToSpeech(text):
    tts.setProperty('voice', 'ru')
    tts.setProperty('rate', 150)
    tts.setProperty('volume', 0.7)
    tts.setProperty('stress_market', True)

    for voice in voices:
        if voice.name == 'Artemiy':
            tts.setProperty('voice', voice.id)

    speech = 'speak.ogg'
    tts.save_to_file(text, speech)
    tts.runAndWait()
    return speech

@bot.message_handler(commands=['start'])
def start(message, res=False):
    bot.send_message(message.chat.id, 'привет!! отправь аудиозапись, а я перефразирую ее в текст')

'''''''''
@bot.message_handler(content_types=['voice'])
def bot_handler_voice(message):
    bot.reply_to(message, 'обрабатываю сообщение..')
    audio = downloadWav(message)
    text = recognizeAudio(audio)

    mess = 'вы сказали' + text
    bot.reply_to(message, mess)
    os.remove(audio)

def downloadWav(message):
    file_info = bot.get_file(message.voice.file_id)
    download_file = bot.download_file(file_info.file_path)

    fileID = file_info.file_id
    src_ogg = fileID + '.ogg'
    src_wav = fileID + '.wav'

    f = open(src_ogg, 'wb')
    f.write(download_file)
    print(f'{src_ogg} сохранен')
    f.close()

    sound = AudioSegment.from_file(src_ogg, format = 'ogg')
    sound.export(src_wav, format='wav')
    os.remove(src_ogg)
    return src_wav
'''''''''
def recognizeAudio(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google_cloud(audio_data, language='ru-RU')
    return text

bot.polling(none_stop=True, interval=0)