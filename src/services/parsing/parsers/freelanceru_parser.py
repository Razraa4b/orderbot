import logging
import aiohttp

from datetime import datetime
from bs4 import BeautifulSoup

from typing import List
from services.parsing import Parser, Order


class FreelanceruParser(Parser):
    async def parse(self) -> List[Order]:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://freelance.ru/project/search") as response:
                content = await response.text()
                soup = BeautifulSoup(content, features="lxml")

                order_elements = soup.select('div.project:not(.highlight)')
                orders = []
                for element in order_elements:
                    try:
                        title = element.find("h2", class_="title")["title"].strip()
                        link = "https://freelance.ru" + element.find("a")["href"]
                        description = element.find("a", class_="description").get_text().strip()
                        publish_time_str = element.find(class_="publish-time")["title"].strip()

                        publish_time = datetime.strptime(publish_time_str, "%Y-%m-%d в %H:%M")
                        orders.append(Order(title, link, description, publish_time))
                    except:
                        continue

                return orders

