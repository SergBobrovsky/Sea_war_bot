from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# ------- Создаем игровую клавиатуру без использования билдера -------


# Создаем объекты инлайн-кнопок
buttons: list[InlineKeyboardButton] = []

keyboard: list[list[InlineKeyboardButton]] = []

for i in range(1, 9):
    for j in range(1, 9):
        buttons.append(InlineKeyboardButton(
        text = '🌊',
        callback_data=f'{i},{j}'))
        if not j % 8:
            keyboard.append(buttons)
            buttons = []

confirm_buttons = []
confirm_buttons.append(InlineKeyboardButton(
        text = LEXICON_RU['confirm_placement'],
        callback_data='confirm_placement'))
confirm_buttons.append(InlineKeyboardButton(
        text = LEXICON_RU['/cancel'],
        callback_data='/cancel'))

keyboard.append(confirm_buttons)

# Создаем игровую клавиатуру с нумерованными кнопками как список списков

pair_AI_game_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
                                    inline_keyboard=keyboard,
                                  resize_keyboard=True)


# Пересоздаем клавиатуру после нажатия кнопки
def rebuild_keyboard(old_board, x, y, status):
	keyboard = old_board
	if status == "empty":
		keyboard[y][x] = InlineKeyboardButton(
        text = '🌊',
        callback_data=f'{x},{y}')
	elif status == "place":
		keyboard[y][x] = InlineKeyboardButton(
        text = '🔲',
        callback_data=f'{x},{y}')
	rebuilt_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup( inline_keyboard=keyboard,
                                  resize_keyboard=True)
	return rebuilt_keyboard