import json
from datetime import datetime, timedelta

from django.core.management import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Создаем интервал для повтора
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )

        # Создаем задачу для повторения
        PeriodicTask.objects.create(
            interval=schedule,
            name=f'Play me',
            task='users.tasks.test_celery',
            expires=datetime.now() + timedelta(days=365),
            start_time=str(datetime.now() + timedelta(minutes=1)),
        )
