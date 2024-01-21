from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from app.internal.services import response_processing
from app.internal.models.user import User
from app.internal.services.get_weather import get_weather
import aiohttp
import os
from dotenv import load_dotenv


load_dotenv()
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']


async def handle_locality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    response = await get_weather(update.effective_message.text)
    #достает текст из сообщения пользока
    if response.status == 404:
        text = 'Населённый пункт не найден, напишите /start чтобы попробовать найти его еще раз 😪'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return ConversationHandler.END
    elif response.status != 200:
        text = 'Технические шоколадки, сервис временно недоступен 😪'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return ConversationHandler.END

    #создать пользователя с айдишником и городом
    user = User(id=update.effective_user.id, city=update.effective_message.text, chat_id=update.effective_chat.id)
    await user.asave()

    data = response.json_parsed
    text = response_processing.generate_recommendations(data)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    text = f'Вы хотите получать такие ежедневные уведомления о погоде в городе  {data["name"]}? Напишите да/нет.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    context.user_data['city'] = data['name']
    return 1
