from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #это импорт, идет в самом начале программы
import logging
import settings

#логирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', #имя-уровеньВажностиСобытия-СообщениеОсобытии
                    level=logging.INFO, #сообщения уровеней INFO,WARNING,ERROR
                    filename='bot.log'
                    )

#объявление функции
def greet_user(bot, update):
    text = 'Call /start'
    logging.info(text)
    update.message.reply_text(text)#бот отвечает в Телеграм

def talk_to_me(bot, update):
    user_text = 'Hello {}! You wrote: {}'.format(update.message.chat.first_name, update.message.text)  #создание переменной
    #.chat.first_name - параметр из бота - см.компендиум
    #print(update.message) #пишу в консоль
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
        update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)#ответ бота в Телеграм пользователю (эхо-бот)

#объявление функции
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY) #ключ для бота, используй прокси
    
    logging.info('Bot begin running')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #ф-ю можем назвать как угодно
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling() #бот, ходи в телеграм
    mybot.idle() #работай бесконечно

#вызов функции
main()
