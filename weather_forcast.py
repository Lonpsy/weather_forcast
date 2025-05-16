from rich import print
import requests


def greetings():
  greetings = print("make sure you dress properly")


def forcast_weather(city):
  days = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
  api_key = 'da7a1b3d460dbtbf7b304o1bb99604f1'
  api_url = f'https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}'
  index = 0

  for day in days:

    response = requests.get(api_url)
    forcast = response.json()
    weather_forcast_minimum = round(
        forcast['daily'][index]['temperature']['minimum'])
    weather_forcast_maximum = round(
        forcast['daily'][index]['temperature']['maximum'])
    print(
        f"{day} : min:{weather_forcast_minimum} max:{weather_forcast_maximum}")
    index = index + 1


city = input("enter your current city ")
forcast_weather(city)

greetings()
