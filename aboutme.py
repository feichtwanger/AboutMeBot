import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    # create btn
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_git = types.KeyboardButton(text='git')
    btn_inst = types.KeyboardButton(text='inst')
    keyboard.add(btn_git, btn_inst)
    
    bot.send_message(chat_id,
                     "Hello, I'm Feicht bot!\nPress the button to find out what you want to know.",
                     reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'git')
def git(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Here is my GitHub:   [My Git](https://github.com/feichtwanger)', parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == 'inst')
def inst(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Here is my Instagram:   [instagram](https://www.instagram.com/kdjdndkkfn/)', parse_mode='Markdown')
    
bot.infinity_polling()