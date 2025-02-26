from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
	name = message.from_user.first_name
	await message.answer(f"Hello {name}!")

