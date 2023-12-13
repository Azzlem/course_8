from celery import shared_task

from config import settings
import requests


@shared_task
def test_celery():
    if True:
        token = '6333151746:AAGTvJNppjNUVtzXbcmQioLGu-ZP3HuhzYg'
        chat_id = settings.CHAT_ID

        params = {
            'chat_id': chat_id,
            'text': f"Я буду "
        }
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
