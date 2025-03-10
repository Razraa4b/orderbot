from typing import List

from abc import ABC, abstractmethod
from .order import Order


class Parser(ABC):
    @abstractmethod
    async def parse(self) -> List[Order]:
        pass
