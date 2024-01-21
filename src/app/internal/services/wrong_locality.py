from telegram import Update
from telegram.ext import ContextTypes


async def wrong_locality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = "Населённый пункт не найден, напишите /start чтобы попробовать найти его еще раз"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    return 1
