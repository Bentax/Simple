import telebot

bot = telebot.TeleBot('1423318538:AAF2GgBfNEEwNtHuzrlI9sLyxgV1awmB5hI')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "{0.first_name}, пиццу хочешь?\nЯ этим не занимаюсь, но ты можешь заказать где-нибудь пиццу... и мы можем поговорить...".format(message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)