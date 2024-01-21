from app.internal.models.user import User
from telegram.ext import CallbackContext
from app.internal.services.get_weather import get_weather
from app.internal.services.response_processing import generate_recommendations

async def send_weather(context: CallbackContext):
    # функция, чтобы делать рассылку
    previous_city = "uffff"
    message = ""
    async for user in User.objects.filter(signed=True).order_by('city'):
        if previous_city != user.city:
            previous_city = user.city
            weather = await get_weather(user.city)
            message = generate_recommendations(weather.json_parsed)
        await context.bot.send_message(chat_id=user.chat_id, text=message)

