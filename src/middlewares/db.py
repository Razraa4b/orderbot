from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from services.database import DatabaseContext
from utils.config import DB_CONNECTION_STRING


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.context = None

    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message, 
        data: Dict[str, Any]
    ) -> Any:
        if not self.context:
            self.context = await DatabaseContext.create(DB_CONNECTION_STRING)
        data["context"] = self.context
        return await handler(event, data)
