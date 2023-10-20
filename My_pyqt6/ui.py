''' Interface Windows'''
import asyncio
import threading
import time
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from view import get_news

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("src/main.ui", self)
        self.show()
        new_thread = threading.Thread(target=self.ex)
        new_thread.start()

    def ex(self):
        asyncio.run(self.another_thread())

    async def another_thread(self):
        time.sleep(1)
        #
        news = await get_news('http://127.0.0.1:8000/api/news/')
        self.ui.label_news.setText(news)
