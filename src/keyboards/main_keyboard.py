from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/active"), KeyboardButton(text="/interval")],
    [KeyboardButton(text="/latest")]
], resize_keyboard=True)
