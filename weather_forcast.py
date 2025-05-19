from rich import print
import requests
from datetime import datetime


def advice():
    advice = print("remember to dress properly")
    print(advice)


def current_weather(city):
    api_key = 'da7a1b3d460dbtbf7b304o1bb99604f1'
    api_url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}'
    response = requests.get(api_url)
    weather_data = response.json()
    today_weather = round(weather_data['temperature']['current'])
    print(f'It is currently {today_weather}°C in {city}')


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

        if formated_date.date() != datetime.today().date():
            print(f'{formated_day}')
            print(
                f"[purple bold]  minmum[/purple bold]:{weather_forcast_minimum}  maximum {weather_forcast_maximum}"
            )
        index = index + 1


city = input("enter your current city ")
print('\n')
current_weather(city)
print('\n')
forcast_weather(city)
print('\n')
advice()
