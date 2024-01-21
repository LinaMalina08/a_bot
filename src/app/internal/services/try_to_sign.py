from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from app.internal.models.user import User


async def try_to_sign(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    city = context.user_data['city']
    del context.user_data['city']
    user_answer = update.message.text
    if user_answer.lower() == "да":
        text = f"Хорошо, теперь буду присылать вам информацию о погоде в городе {city}."
        # Подписать пользователя на рассылку
        await User.objects.filter(id=update.effective_user.id).aupdate(signed=True)

        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return ConversationHandler.END
    elif user_answer.lower() == "нет":
        text = "Хорошо, если захотите подключить уведомления о погоде, напишите мне /start"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return ConversationHandler.END
    else:
        text = "Неправильный формат ввода, напишите /start, чтобы попробовать еще раз"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return ConversationHandler.END
