from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):

   welcome='''Здравствуйте! Я бот "Too Easy Travel" и помогу Вам выбрать отель мечты.
    География поиска - весь мир. Я покажу вам сайты и фоторгафйии понравившихся отелей
    в соответствии с выбраными Вами характеристиками. Приступим.  
   '''
   bot.reply_to(message, welcome)
    #bot.reply_to(message, f"Привет, {message.from_user.full_name}!")

