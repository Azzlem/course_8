from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask


class Command(BaseCommand):

    def handle(self, *args, **options):
        PeriodicTask.objects.all().delete()
