# Создайте программу для игры с конфетами человек против бота(интелект).

import secret # токен бота лежит в файле secret.py, который добавлен в .gitignore, чтобы не публиковать его на весь интернет
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler
from random import randint

start_candies = 2021
candies_on_table = start_candies
candies_limit = 28

bot = Bot(token = secret.key)
updater = Updater(token = secret.key)
dispatcher = updater.dispatcher

A = 0

def start(update, context):
	global candies_on_table
	global start_candies
	global candies_limit
	candies_on_table = start_candies
	context.bot.send_message(update.effective_chat.id, f'Привет!\nНачинаем игру в конфеты\nДля прерывания игры введите "/cancel"\nНа столе {candies_on_table} конфет.\nЗа один ход можно взять не более {candies_limit} конфет\nСколько конфет хотите взять?')

	return A

def game(update, context):
	global candies_on_table
	global start_candies
	global candies_limit
	text = update.message.text
	try:
		if int(text) <= min(candies_on_table, candies_limit) and int(text) > 0:
			candies_on_table -= int(text)
			if candies_on_table <= 0:
				context.bot.send_message(update.effective_chat.id, 'Поздравляю!\nВы выйграли!!!')
				return ConversationHandler.END
			else:
				context.bot.send_message(update.effective_chat.id, f'На столе осталось {candies_on_table} конфет')
				candies = candies_on_table % (candies_limit + 1)
				if not candies:
					candies = randint(1, min(candies_on_table, candies_limit))
				context.bot.send_message(update.effective_chat.id, f'Бот забирает конфет\n{candies}')
				candies_on_table -= candies
				if candies_on_table <= 0:
					context.bot.send_message(update.effective_chat.id, 'Вы проиграли')
					return ConversationHandler.END
				else:
					context.bot.send_message(update.effective_chat.id, f'На столе осталось {candies_on_table} конфет\nСколько конфет хотите взять?')
					return A
		else:
			context.bot.send_message(update.effective_chat.id, 'Ошибка ввода!\nВведите значение повторно')
			return A
	except:
		context.bot.send_message(update.effective_chat.id, 'Ошибка ввода!\nВведите значение повторно')
		return A

def cancel(update, context):
	context.bot.send_message(update.effective_chat.id, 'Игра прервана!')
	return ConversationHandler.END

start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
game_handler = MessageHandler(Filters.text & ~Filters.command, game)
conv_handler = ConversationHandler(entry_points = [start_handler],
									states = {A: [game_handler]},
									fallbacks = [cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
