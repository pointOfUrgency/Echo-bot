import telebot


bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi! I am a test bot. I created by Urg.')


@bot.message_handler()
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
