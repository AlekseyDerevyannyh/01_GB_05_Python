# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

import secret # токен бота лежит в файле secret.py, который добавлен в .gitignore, чтобы не публиковать его на весь интернет
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token = secret.key)
updater = Updater(token = secret.key)
dispatcher = updater.dispatcher

def remove_abv(update, context):
	text = update.message.text.split()
	bot_answer = []
	for i in text:
		if 'абв' not in i:
			bot_answer.append(i)
	if bot_answer:	context.bot.send_message(update.effective_chat.id, (' ').join(bot_answer))
	else:			context.bot.send_message(update.effective_chat.id, 'null')

message_handler = MessageHandler(Filters.text, remove_abv)

dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
