import logging
import os
from app.internal.handlers.start import start
from app.internal.services.handle_locality import handle_locality
from app.internal.services.try_to_sign import try_to_sign
from app.internal.handlers.cancel import cancel
from app.internal.services.send_weather import send_weather
import datetime

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

SEND_LOCALITY, RESPONSE = range(2)

class Bot:
    application = None

    def add_handler(self, handler) -> None:
        self.application.add_handler(handler)

    def init_bot(self) -> None:
        bot_token = os.environ['BOT_TOKEN']
        self.application = ApplicationBuilder().token(bot_token).build()
        self.application.job_queue.run_daily(callback=send_weather, time=datetime.time(5, 0, 0))
        #self.application.job_queue.run_repeating(callback=send_weather, interval=5)
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                SEND_LOCALITY: [MessageHandler(~filters.COMMAND & filters.TEXT, handle_locality)],
                RESPONSE: [MessageHandler(~filters.COMMAND & filters.TEXT, try_to_sign)]
            },
            fallbacks=[MessageHandler(filters.Regex("^$"), cancel)],
        )
        self.application.add_handler(CommandHandler("cancel", cancel))
        self.application.add_handler(conv_handler)

    def run_bot(self) -> None:
        self.application.run_polling()
