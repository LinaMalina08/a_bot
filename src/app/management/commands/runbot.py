import telegram.error
from django.core.management.base import BaseCommand
from app.internal.bot import Bot


class Command(BaseCommand):
    help = "Runs the telegram bot in poll mode."

    def handle(self, *args, **options):
        bot = Bot()
        try:
            bot.init_bot()
            #открыть файл с ботом
            bot.run_bot()
            #запустить бота
        except telegram.error.InvalidToken:
            self.stdout.write(self.style.ERROR("Error. Bot has a bad token..."))
