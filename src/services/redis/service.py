from typing import List, Any

from .connection import get_connection
from .operations import set, get, push, lrange, set_expire


class RedisService:
    def __init__(self, url: str):
        self._url = url
        self._conn = None

    async def connect(self) -> None:
        if not self._conn:
            self._conn = await get_connection(self._url)

    async def set(self, key: str, value: str, expire_time: int = None) -> None:
        if self._conn:
            await set(self._conn, key, value, expire_time)

    async def get(self, key: str) -> Any:
        if self._conn:
            result = await get(self._conn, key)
            return result
        
    async def push(self, key: str, new_items: List[Any]) -> None:
        if self._conn:
            await push(self._conn, key, new_items)

    async def expire(self, key: str, expire_time: int) -> None:
        if self._conn:
            await set_expire(self._conn, key, expire_time)

    async def lrange(self, key: str, start: int, end: int) -> List:
        if self._conn:
            return (await lrange(self._conn, key, start, end))[0]
