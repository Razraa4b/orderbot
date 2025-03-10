from datetime import datetime


class Order:
    def __init__(self, title: str, link: str, description: str, elapsed_time: str = None, publish_time: datetime = None):
        self.title = title
        self.link = link
        self.description = description
        self.elapsed_time = elapsed_time
        self.publish_time = publish_time