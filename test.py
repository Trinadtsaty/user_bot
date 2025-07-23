from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from hide.key import key

# Вставьте свои данные
api_id = key["user1"]["api_id"]  # Ваш API ID с my.telegram.org
api_hash = key["user1"]["api_hash"]  # Ваш API HASH
phone = key["user1"]["phone"]  # Ваш номер телефона

# Создаем клиент
client = TelegramClient('test_session', api_id, api_hash)

try:
    # Подключаемся
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

    group_link = "https://t.me/+l_gqRHiADUE3YzU6"
    def send_message(client, group_link, text_message):
        group = client.get_entity(group_link)
        client.send_message(group.id, text_message)


    def ckek_message(client, group_link):
        pass

    # def get_messages(client, group_link):
    #     group = client.get_entity(group_link)
    #     last_msg = client.get_messages(group.id, limit=1)
    #     if  last_msg:
    #         approx_count = last_msg[0].id
    #         print(f"Примерное количество сообщений: {approx_count}")
    #         messages = client.get_messages(group.id, limit=approx_count)
    #     else:
    #         messages = client.get_messages(group.id, limit=100)
    #     send_message=""
    #     i=0
    #     for message in messages:
    #         sender = message.sender
    #         if sender:
    #             if hasattr(sender, 'username') and sender.username:  # Если есть username
    #                 sender_name = f"@ {sender.username}"
    #             else:
    #                 sender_name = get_display_name(sender)  # Имя + фамилия или название группы
    #         else:
    #             sender_name = "Неизвестный отправитель"
    #
    #         i+=1
    #         text = message.text or "Нет текста"
    #         ma = f"""
    #     сообщение: {i}
    #     ID сообщения:{message.id}
    #     Дата: {message.date}
    #     Отправитель id: {message.sender_id}
    #     Отправитель ник: {sender_name}
    #     Текст (первые 20 символов): {text[:20]}
    #     Тип: {'пост' if message.post else 'обычное'}
    #     \n
    #     """
    #         send_message+=ma
    #
    #     return send_message

    # Отправляем себе сообщение
    # client.send_message('me', 'https://t.me/+m3RLtBuZP0o3MDJi')
    # print('Сообщение отправлено в "Сохранённые"!')

except Exception as e:
    print(f'Произошла ошибка: {e}')

finally:
    # Закрываем соединение
    send_message(client, group_link,get_messages(client, group_link))
    client.disconnect()
    print('Работа завершена')