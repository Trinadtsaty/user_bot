from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os

from hide.key import key
api_id = key["user1"]["api_id"]  # Ваш API ID с my.telegram.org
api_hash = key["user1"]["api_hash"]  # Ваш API HASH
phone = key["user1"]["phone"]  # Ваш номер телефона

client = TelegramClient('test_session', api_id, api_hash)

# Указываем директорию для хранения сессий
session_directory = 'sessions'  # Папка sessions в текущей директории

# Создаём папку, если её нет
os.makedirs(session_directory, exist_ok=True)

client = TelegramClient(
    session=os.path.join(session_directory, 'bot1'),  # Путь к файлу сессии
    api_id=api_id,
    api_hash=api_hash
)
try:
    client.connect()

    # Если не авторизованы, просим код
    if not client.is_user_authorized():
        client.send_code_request(phone)
        code = input('Введите код из Telegram: ')
        try:
            client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = key["user1"]["password"]
            client.sign_in(password=password)

except Exception as e:
    print(f'Произошла ошибка: {e}')

finally:
    # Закрываем соединение
    client.disconnect()
    print('Работа завершена')
