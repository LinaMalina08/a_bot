from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
import datetime

code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }


def generate_recommendations(data: dict) -> str:
    result = ['На сегодня я собрал следующую информацию o погоде:']

    city = data["name"]
    current_temp = round(data["main"]["temp"])
    wind = data["wind"]["speed"]
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'])
    weather_description = data['weather'][0]['main']

    if current_temp < -10:
        text = f'На улице {current_temp} °C, не забудьте взять варежки и теплый шарф!'
        result.append(text)
    if wind >= 10:
        text = "Сегодня сильный ветер, будьте осторожны."
    if weather_description == "Rain" or weather_description == "Drizzle":
        text = "Возможен дождь, обязательно возьмите зонт."
        result.append(text)
    if current_temp >= 25:
        text = "Сегодня будет жара, оденьте панамку и не находитесь днём долго на солнце."
        result.append(text)
    if weather_description == "Snow":
        text = "Из-за снега могут быть пробки, планируйте своё время!"
        result.append(text)
    if weather_description == "Thunderstorm":
        text = "Сегодня возможна гроза, будьте аккуратны, возьмите зонт."
        result.append(text)
    if weather_description not in code_to_smile:
        text = "Что за погода на улице, я не понимаю..."
        result.append(text)
    result.append(f'Температура: {current_temp} °C')
    result.append(f'Восход солнца: {sunrise}')
    result.append(f'Заход солнца: {sunset}')
    result.append(" ")
    result.append("Продуктивного дня, до завтра!")
    return '\n'.join(result)
