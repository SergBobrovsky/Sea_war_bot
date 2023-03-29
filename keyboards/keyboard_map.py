from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# ------- Создаем игровую клавиатуру без использования билдера -------


# Создаем объекты инлайн-кнопок
buttons: list[InlineKeyboardButton] = []

keyboard: list[list[InlineKeyboardButton]] = []

for i in range(1, 9):
    for j in range(1, 9):
        buttons.append(InlineKeyboardButton(
        text = '*',
        callback_data=f'{i},{j}'))
        if not j % 8:
            keyboard.append(buttons)
            buttons = []


# Создаем игровую клавиатуру с нумерованными кнопками как список списков

game_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
                                    inline_keyboard=keyboard,
                                  resize_keyboard=True)

# Пересоздаем клавиатуру после нажатия кнопки

def rebuild_keyboard(old_board, x, y, status):
	keyboard = old_board
	if status == "miss":
		keyboard[y][x] = InlineKeyboardButton(
        text = '🌊',
        callback_data=f'{x},{y}')
	elif status == "hit":
		keyboard[y][x] = InlineKeyboardButton(
        text = '💥',
        callback_data=f'{x},{y}')
	elif status == "killed":
		keyboard[y][x] = InlineKeyboardButton(
        text = '💥',
        callback_data=f'{x},{y}')
	rebuilt_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup( inline_keyboard=keyboard,
                                  resize_keyboard=True)
	return rebuilt_keyboard