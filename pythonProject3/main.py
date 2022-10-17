import telebot
import configure
import requests
from bs4 import BeautifulSoup
import lxml

bot = telebot.TeleBot(configure.config['token'])

def players(name):
    sus = []
    url = f"https://steamcharts.com/app/{configure.list_games[name]}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    schet = soup.find_all(class_='num')
    for i in schet:
        sus.append(i.text.strip())
    return name.split('.')[1] + ' = ' + sus[0]

def games():
    game_names = "\n".join(configure.list_games.keys())
    return game_names

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Узнать онлайн в игре из списка:\n\n" + games())

@bot.message_handler(content_types='text')
def user_message(message):
    if message.text in configure.numbers_games.keys():
        bot.send_message(message.chat.id, players(configure.numbers_games[message.text]))
    else:
        bot.send_message(message.chat.id, "Пошёл нахуй!!!!!!!!!!!!!!!!!!")

bot.polling(non_stop=True, interval=0)

