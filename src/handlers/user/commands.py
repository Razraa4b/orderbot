from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import interval_keyboard

from services.database.models import User, UserBotSettings
from services.database import DatabaseContext


router = Router()


@router.message(Command("active"))
async def active_cmd(message: Message, context: DatabaseContext):
    telegram_id = message.from_user.id
    user: User = await context.get(User, User.telegram_id == telegram_id, [User.bot_settings])
    
    if not user.bot_settings.is_active:
        await context.update(UserBotSettings, UserBotSettings.user_id == user.id, is_active=True)
        await message.answer("Now the bot is active for you ✅")
    else:
        await context.update(UserBotSettings, UserBotSettings.user_id == user.id, is_active=False)
        await message.answer("Now the bot is inactive for you ❌")

@router.message(Command("interval"))
async def interval_cmd(message: Message):
    await message.answer("Select the interval for sending new orders when available",
                         reply_markup=interval_keyboard)

@router.message(Command("latest"))
async def latest_cmd(message: Message):
    pass
