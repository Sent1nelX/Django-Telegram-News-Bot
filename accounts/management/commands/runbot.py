from django.core.management.base import BaseCommand
from accounts.bot import RunBot


class Command(BaseCommand):
    help = 'Run Bot'

    def handle(self, *args, **options):
        RunBot()




# python3 manage.py runserver
# python3 manage.py runbot