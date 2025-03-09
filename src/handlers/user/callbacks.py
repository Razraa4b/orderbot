from aiogram import Router, F
from aiogram.types import CallbackQuery

from services.database.models import User, UserBotSettings
from services.database import DatabaseContext


router = Router()


@router.callback_query(F.data.startswith("set_interval"))
async def set_interval_callback(callback: CallbackQuery, context: DatabaseContext):
    telegram_id = callback.from_user.id
    seconds = int(callback.data.replace("set_interval_", ""))

    user: User = await context.get(User, User.telegram_id == telegram_id, [User.bot_settings])
    await context.update(UserBotSettings, UserBotSettings.user_id == user.id, mail_interval=seconds)

    await callback.answer(f"Set interval {seconds} seconds")
