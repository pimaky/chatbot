import telebot

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

bot = telebot.TeleBot('6445698865:AAHTFW8ptLPgrrba08DQfNuHZjf6Nk2BoYg')

driver = webdriver.Chrome()

@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'привет!!\n'
                                      'я помогу тебе найти видео с youtube!!\n'
                                      'для поиска напиши /search_videos')

@bot.message_handler(commands=["search_videos"])
def search_videos(message):
    msg = bot.send_message(message.chat.id, "введите текст, который вы хотели найти в youtube.")
    bot.register_next_step_handler(msg, search)

@bot.message_handler(content_types=["text"])
def text(message):
    bot.send_message(message.chat.id, "ты что-то хотел??")

def search(message):
    bot.send_message(message.chat.id, "начинаю поиск..")
    video_href = "https://www.youtube.com/results?search_query=" + message.text
    driver.get(video_href)
    sleep(5)
    videos = driver.find_elements(By.ID, "video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 3:
            break
bot.polling(none_stop=True, interval=0)