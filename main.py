import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('***')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Приветствуем! '
                                '\nЭтот бот создан для того, чтобы заранее задать вопрос по Писанию, жизни церкви, хождению перед Богом. '
                                '\nБратья-служители постараются ответить на этот вопрос на ближайших библейских курсах для членов церкви.')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ваш вопрос: "' + message.text + '" принят в разработку. '
                                                                       '\nЖелаем вам Божьих благословений!')
    bot.send_message(0, 'Поступил анонимный вопрос: \n"'+ message.text+'"')
# Запускаем бота
bot.polling(none_stop=True, interval=0)