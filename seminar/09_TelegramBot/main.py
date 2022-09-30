# pip install python-telegram-bot
import secret
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd

bot = Bot(token = secret.key)
updater = Updater(token = secret.key)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(update.effective_chat.id, 'Hello')

def rand(update, context):
	context.bot.send_message(update.effective_chat.id, f'{rd(1,100)}')

def voice(update, context):
	context.bot.send_message(update.effective_chat.id, 'Я пока таких команд не знаю :(')

start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', rand)
message_handler = MessageHandler(Filters.command, voice)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
