#example url api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid={API key}

import os
from sqlite3 import Timestamp
import requests
from pprint import pprint
from datetime import datetime

url = 'http://api.openweathermap.org/data/2.5/forecast'
key = os.environ.get('WEATHER_KEY')


def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key) #will save return value in tuple of eather_data and error
    if error:
        print('Sorry, could not get wather')
    else:
        current_temp = get_temp(weather_data) # if no error get_temp function is called
        print(f'The current temperature is {current_temp}F')


def get_location():
    city, country = '', '' # checking input is not empty string
    while len(city)==0:
        city = input('Enter the city: ').strip()

    while len(country) != 2 or not country.isalpha(): # checks that data entered are two characters and that are letters
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city},{country}'
    return location


def get_current_weather(location, key):
    try:
        query ={'q': location, 'units': 'imperial', 'appid': key} #query string
        response = requests.get(url, params=query)
        response.raise_for_status()#raise exception for 400 or 500 errors
        data = response.json()#may error if response is not json
        list_of_forecasts = data['list']

        for forecast in list_of_forecasts:
            temp = forecast['main'] ['temp']
            timestamp = forecast['dt']
            forecast_date = datetime.fromtimestamp(timestamp)
            print(f'At {forecast_date} the temperature will be {temp}F')
            
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text) #for debugging print, might want to log for developing 
        return None, ex

def get_temp(weather_data):
    try:
        temp = weather_data['main'] ['temp']
        return temp
    except KeyError:
        print('This data is not in the format expected')
        return 'Unknown'


if __name__ == '__main__':
    main()