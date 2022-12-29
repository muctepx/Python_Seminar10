from datetime import datetime
import telebot
from pycbrf import ExchangeRates

bot = telebot.TeleBot('5757879125:AAFE9HYXzh5BIP8STyjXUgXL1rvX27SHAZA')

@bot.message_handler(commands=['ex'])
def ex(message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = telebot.types.KeyboardButton('USD')
        btn2 = telebot.types.KeyboardButton('EUR')
        btn3 = telebot.types.KeyboardButton('CNY')
        btn4 = telebot.types.KeyboardButton('GBP')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id=message.chat.id, text='Курс валют. Выберите валюту:', reply_markup=markup, parse_mode="html")

@bot.message_handler(content_types=['text'])
def message(message):
        message_user = message.text.strip().lower()

        if message_user in ['usd', 'eur', 'cny', 'gbp']:
                rates = ExchangeRates(datetime.now())
                bot.send_message(chat_id=message.chat.id, text=f"Курс {message_user.upper()} = {float(rates[message_user.upper()].rate)}", parse_mode="html")
        else:
                bot.send_message(chat_id=message.chat.id, text=f"Такой валюты нет в базе")

bot.polling(none_stop=True)