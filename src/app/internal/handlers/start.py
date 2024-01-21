from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = "Привет, назовите имя своего населённого пункта"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    return 0
