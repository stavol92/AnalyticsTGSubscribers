import asyncio
from django.core.management.base import BaseCommand, CommandError

from core.apps.bot.main_bot import bot


class Command(BaseCommand):
    help = "Start Bot"


    def handle(self, *args, **options):
        asyncio.run(bot.polling())
