import telebot
print("Im simple bot for telegram")
tokenx = input("Enter bot token:")
bot = telebot.TeleBot(tokenx)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Hello! Send some message')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True, interval=0)