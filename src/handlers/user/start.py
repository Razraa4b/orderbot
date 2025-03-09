from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_keyboard

from services.database.models import User, UserBotSettings
from services.database import DatabaseContext

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message, context: DatabaseContext):
	username = message.from_user.username
	telegram_id = message.from_user.id

	if not (await context.get(User, User.telegram_id == telegram_id)):
		new_user = User(username=username, telegram_id=telegram_id)
		new_user.bot_settings = UserBotSettings()
		await context.add(new_user)

	await message.answer(f"What\'s up {message.from_user.first_name}! I am a bot that will track new orders" + 
					  	   "on exchanges instead of you, and in case of a new order, notify you.",
						   reply_markup=main_keyboard)
