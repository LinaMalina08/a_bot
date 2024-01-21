from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from app.internal.models.user import User


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user = await User.objects.aget(id=update.effective_user.id)
        user.signed = False
        await user.asave()
        text = "До свидания!"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except User.DoesNotExist:
        text = "Вы еще не зарегистрированы, воспользуйтесь командой /start"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
