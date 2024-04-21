import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm_token = "e9c11364ee9b8558db71f35404174dbc"
bot = telebot.TeleBot("6765050326:AAHHvvW-RaM-aMJGX5pRgXmk-v4p_jcn7_g")

@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'привет!!\n'
                                      'я помогу тебе узнать сколько градусов на улице!!\n'
                                      'для поиска напиши /search_city')

@bot.message_handler(commands=["weather"])
def search_city(message):
    msg = bot.send_message(message.chat.id, "введите город.")
    bot.register_next_step_handler(msg, weather)
def weather(message):
    city = message.text
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM(owm_token, config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    status = weather.detailed_status
    temperature = weather.temperature("celsius")
    print(temperature)
    print(status)
    temp = round(temperature['temp'])
    feels_like = round(temperature['feels_like'])
    msg = "в городе " + city + "\nсейчас " + status + "\n" + str(temp) + " градусов.\nощущается как " + str(feels_like)
    bot.send.message(message.chat.id, msg)

@bot.message_handler(commands=["search"])
def search(message):
    msg = bot.send_message(message.chat.id, "введите город, которого вы хотите узнать температуру.")
    bot.register_next_step_handler(msg, search)

weather("Ростов-на-Дону")

bot.polling(none_stop=True, interval=0)