from rich import print
import requests
from datetime import datetime


def advice():
    advice = print("remember to dress properly")
    print(advice)


def forcast_weather(city):
    api_key = 'da7a1b3d460dbtbf7b304o1bb99604f1'
    api_url = f'https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}'
    index = 0
    response = requests.get(api_url)
    forcast = response.json()
    for day in forcast['daily']:
        timestamp = day['time']
        formated_date = datetime.fromtimestamp(timestamp)
        formated_day = formated_date.strftime('%A')
        today = round(day['temperature']['day'])
        weather_forcast_minimum = round(day['temperature']['minimum'])
        weather_forcast_maximum = round(day['temperature']['maximum'])
        print(f'{formated_day}')
        print(
            f"{today} : [purple bold]  minmum[/purple bold]:{weather_forcast_minimum}  maximum {weather_forcast_maximum}"
        )
        index = index + 1


city = input("enter your current city ")
forcast_weather(city)
print('\n')
advice()
