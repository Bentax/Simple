import telebot

bot = telebot.Telebot('1423318538:AAF2GgBfNEEwNtHuzrlI9sLyxgV1awmB5hI')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)