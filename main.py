from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os
from hide.key import key

# session_directory = 'sessions'

class TelegramBot_Chat:
    def __init__(self, api_id: int, api_hash: str, phone: str, password: str, name: str, folder:str):

        self.client = TelegramClient(
            session=os.path.join(folder, name),  # Путь к файлу сессии
            api_id=api_id,
            api_hash=api_hash
        )

    def register_handlers(self):

        self.client.connect()


