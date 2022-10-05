# 1. Добавить счёт, сколько раз выиграл бот и пользователь
# Необходимо добавить новую команду, при вызове которой, бот говорит, кто сколько раз выйграл (выводит счёт)

import secret	# токен бота лежит в файле secret.py, который добавлен в .gitignore, чтобы не публиковать его на весь интернет
from telegram import Bot
from telegram.ext import Updater, CommandHandler

from scripts import check
from random import choice as ch

bot = Bot(token = secret.key)
updater = Updater(token = secret.key)
dispatcher = updater.dispatcher

data = {6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 'Валет': 4, 'Дама': 4, 'Король': 4, 'Туз': 4}

count_user_win = 0
count_bot_win = 0
count_points_user = []
count_points_bot = 0
game_over = False

WINNER = None # 0 - ничья, 1 - выиграл пользователь, -1 - выиграл бот,

def winner_check(user, bots):
	global WINNER
	if sum(user) > 21:
		if bots > 21:
			WINNER = 0
		else:
			WINNER = -1
	elif sum(user) == 21:
		if bots == 21:
			WINNER = 0
		else:
			WINNER = 1
	else:
		if bots > 21:
			WINNER = 1
		else:
			if sum(user) > bots:
				WINNER = 1
			elif sum(user) < bots:
				WINNER = -1
			else:
				WINNER = 0

def start(update, context):
	global count_points_user, count_points_bot, WINNER
	global count_user_win, count_bot_win, game_over
	global data
	data = {6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 'Валет': 4, 'Дама': 4, 'Король': 4, 'Туз': 4}
	game_over = False
	count_points_user.clear()
	count_points_bot = 0
	WINNER = None

	context.bot.send_message(update.effective_chat.id, "Начинаем игру в 21\nДоступные команды:\n/start - запуск игры\n/yet - взять ещё одну карту\n/stop - закончить набор карт\n/score - посмотреть счёт\n/reset - сбросить счёт")

	for i in range(2):
		data_object = ch(list(data.keys()))
		while data[data_object] == 0:
			data_object = ch(list(data.keys()))
		data[data_object] -= 1
		points = check(data_object)
		count_points_user.append(points)

	for i in range(2):
		data_object = ch(list(data.keys()))
		while data[data_object] == 0:
			data_object = ch(list(data.keys()))
		data[data_object] -= 1
		points = check(data_object)
		count_points_bot += points

	a = '\n'.join([str(i) for i in count_points_user])
	context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")
	
	if sum(count_points_user) > 21 and count_points_bot < 22:
		context.bot.send_message(update.effective_chat.id, "У вас перебор. Выиграл бот")
		context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
		count_bot_win += 1
		game_over = True
	elif count_points_bot > 21 and sum(count_points_user) < 22:
		context.bot.send_message(update.effective_chat.id, "У бота перебор. Вы выиграли!")
		context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
		count_user_win += 1
		game_over = True
	elif sum(count_points_user) > 21 and count_points_bot > 21:
		context.bot.send_message(update.effective_chat.id, "У вас и у бота перебор. Ничья")
		context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
		game_over = True

def yet(update, context):
	global count_points_user
	global count_bot_win
	global count_user_win
	global game_over
	if not game_over:
		if sum(count_points_user) < 21:
			data_object = ch(list(data.keys()))
			while data[data_object] == 0:
				data_object = ch(list(data.keys()))
			data[data_object] -= 1
			points = check(data_object)
			count_points_user.append(points)

			a = '\n'.join([str(i) for i in count_points_user])
			context.bot.send_message(update.effective_chat.id, f"{a}\nСумма: {sum(count_points_user)}")
			if sum(count_points_user) > 21 and count_points_bot < 22:
				context.bot.send_message(update.effective_chat.id, "У вас перебор. Выиграл бот")

				context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
				count_bot_win += 1
				game_over = True
			elif count_points_bot > 21 and sum(count_points_user) < 22:
				context.bot.send_message(update.effective_chat.id, "У бота перебор. Вы выиграли!")
				context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
				count_user_win += 1
				game_over = True
			elif sum(count_points_user) > 21 and count_points_bot > 21:
				context.bot.send_message(update.effective_chat.id, "У вас и у бота перебор. Ничья")
				context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
				game_over = True
		else:
			context.bot.send_message(update.effective_chat.id, "Вы не можете взять больше! Введите /stop для передачи хода боту")
	else:
		context.bot.send_message(update.effective_chat.id, "Игра окончена. Для перезапуска введите /start")

def stop(update, context):
	global count_bot_win
	global count_user_win
	global game_over
	if WINNER == None:
		global count_points_bot
		context.bot.send_message(update.effective_chat.id, 'Вы закончили набор, теперь набирает бот')
		while (count_points_bot <= 15):
			data_object = ch(list(data.keys()))
			while data[data_object] == 0:
				data_object = ch(list(data.keys()))
			data[data_object] -= 1
			points = check(data_object)
			count_points_bot += points
		if count_points_bot > 15 and ch([True, False]):
			data_object = ch(list(data.keys()))
			while data[data_object] == 0:
				data_object = ch(list(data.keys()))
			data[data_object] -= 1
			points = check(data_object)
			count_points_bot += points

		winner_check(count_points_user, count_points_bot)
		context.bot.send_message(update.effective_chat.id, f'Кол-во очков у бота: {count_points_bot}\n'
															f'Кол-во очков у {update.effective_user.first_name}: {sum(count_points_user)}')
		if WINNER == -1:
			context.bot.send_message(update.effective_chat.id, "Выиграл бот")
			count_bot_win += 1
		elif WINNER == 1:
			context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name}, вы выиграли")
			count_user_win += 1
		elif WINNER == 0:
			context.bot.send_message(update.effective_chat.id, f"{update.effective_user.first_name} у вас ничья")
	context.bot.send_message(update.effective_chat.id, f"Игра окончена, чтобы начать заново напишите /start")
	game_over = True

def score(update, context):
	global count_bot_win
	global count_user_win
	context.bot.send_message(update.effective_chat.id, f"Бот выиграл {count_bot_win} раз\n{update.effective_user.first_name} выиграл {count_user_win} раз")

def reset_score(update, context):
	global count_bot_win
	global count_user_win
	count_bot_win = 0
	count_user_win = 0
	context.bot.send_message(update.effective_chat.id, f'Статистика сброшена')

start_handler = CommandHandler('start', start)
still_handler = CommandHandler('yet', yet)
stop_handler = CommandHandler('stop', stop)
score_handler = CommandHandler('score', score)
reset_handler = CommandHandler('reset', reset_score)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(still_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(score_handler)
dispatcher.add_handler(reset_handler)

updater.start_polling()
updater.idle()  # ctrl + c
