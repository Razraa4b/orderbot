from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


interval_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="10s", callback_data="set_interval_10"), InlineKeyboardButton(text="30s", callback_data="set_interval_30")],
    [InlineKeyboardButton(text="60s", callback_data="set_interval_60"), InlineKeyboardButton(text="5m", callback_data="set_interval_300")],
    [InlineKeyboardButton(text="30m", callback_data="set_interval_1800"), InlineKeyboardButton(text="1h", callback_data="set_interval_3600")]
], resize_keyboard=True)
