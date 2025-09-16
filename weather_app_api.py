"""Weathe app using API"""

import requests

def weather_app():
    print("---Welcome to Weather app---")
    city = input("Enter the city name : ")


    #API Key
   # api_key = "0d7d0ae3772be255d131407635c43333"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
             temp = data["main"]["temp"]
             feels_like = data["main"]["feels_like"]
             windspeed = data["wind"]["speed"]
             humidity = data["main"]["humidity"]

             print(f"The Temperature of {city} is {temp}")
             print(f"it feels like {feels_like}")
             print(f"The Humidity is {humidity}")
             print(f"The Wind speed calculated is {windspeed}")

        else :
             print("City not found or API error")


    except Exception as e:
           print("Error",e)



weather_app()
