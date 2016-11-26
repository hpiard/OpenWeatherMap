#!/usr/bin/python3.4

import urllib.request
import xml.etree.ElementTree as ET
import sys

'''
author = 'hpiard'
Python script to retrieve weather data from openweathermap.org
'''

if len(sys.argv) < 2:
    print("Usage:\n" + sys.argv[0] + " Country Code " + "Zip Code")
    print("Example:\n" + sys.argv[0] + " US " + "03087")
    quit()
else:
    # zip_code=("03087")
    country_code = sys.argv[1]
    zip_code = sys.argv[2]
    '''Replace with respective API key of yours'''
    api_key="0e2078414d5d3b745ea616236ba00bd5"
    api_call="http://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + "," + country_code + \
             "&appid=" +api_key + "&mode=xml"
    # print(api_call)
    # print(api_call)


def get_weather_data():
    with urllib.request.urlopen(api_call) as response:
        weather_data = response.read()
        # print(weather_data)
        # file = open("weather_day_windham_nh", "w")
        # file.write(str(weather_data))
        # file.close()
        root = ET.fromstring(weather_data)
    # for child in root:
        # print(child.tag, child.attrib)
        for city in root.findall("city"):
            name = city.get("name")
            name_formatted = str("City: " + name)
        for temperature in root.findall("temperature"):
            temperature = float(temperature.get("value"))
            temperature_in_celsius = temperature - 273.15
            temperature_in_celsius_formatted = str("Temperature: " + "%.2f" % temperature_in_celsius + " Celsius")
        for humidity in root.findall("humidity"):
            humidity = humidity.get("value")
            humidity_formatted = str("Humidity: " + humidity + "%")
        for clouds in root.findall("clouds"):
            clouds = clouds.get("name")
            clouds_formatted = str("Clouds: " + clouds.upper())
    #weather = [name, temperature_in_celsius, humidity, clouds]
    weather = [name_formatted, temperature_in_celsius_formatted, humidity_formatted, clouds_formatted]
    #print(weather)
    return weather

get_weather_data()
