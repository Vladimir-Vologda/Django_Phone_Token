import random

import requests


def send_code(phone):
    try:
        #   Генерация случайных чисел
        #   для создания кода,
        #   состоящего из 5-ти цифр
        verified_code = random.randint(10000, 99999)
        #   Отправка кода на номер пользователя
        url = f'https://sms.ru/sms/send?api_id={"Ваш API_ID"}&to={phone}&msg={verified_code}&json=1'
        response = requests.get(url)
        return verified_code

    except Exception:
        return None
