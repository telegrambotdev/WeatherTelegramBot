import requests
import telebot
import json


token = <your telegram bot token>
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, 'Welcome to our weather bot. Enter your city')


@bot.message_handler(content_types=['text'])
def weather(message):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    city = message.text
    r = requests.post(url = api_url, params = {'q' : city, 'APPID' : '<your API>', 'units' : 'metric'})
    if r.status_code == 200:
        
        response = json.loads(r.content)
        temp = str(response['main']['temp'])
        max_temp = str(response['main']['temp_max'])
        min_temp = str(response['main']['temp_min'])
        wind_speed = str(response['wind']['speed'])
        pressure = str(response['main']['pressure'])
        humidity = str(response['main']['humidity'])

        msg = 'The current weather in ' + city + ' ' + temp + '°C' + '\n' + 'Maximum temperature: ' + max_temp + '°C' + '\n' + 'Minimum temperature: ' + min_temp + '°C' + '\n' + 'Wind speed: ' + wind_speed + '\n' + 'Pressure: ' + pressure + '\n' + 'Humidity: ' + humidity

        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, 'Sorry, I was not able to get a temperature. Please check your name of the city!')

bot.polling(none_stop=True)
