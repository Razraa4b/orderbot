from datetime import datetime


class Order:
    def __init__(self, title: str, link: str, description: str, publish_time: datetime = None):
        self.title = title
        self.link = link
        self.description = description
        self.publish_time = publish_time

    def __hash__(self):
        return hash(self.link)