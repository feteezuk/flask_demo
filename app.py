from flask import Flask, render_template
import pandas as pd
import requests
#files I've created and imported
from name_the_city_to_search_for import CITY_NAME
from config import API_KEY


app = Flask(__name__)

API_KEY_INFO = API_KEY
CITY_NAME_INFO = CITY_NAME


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/index')
def blue():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')



@app.route('/change/')
def he():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME_INFO}&appid={API_KEY_INFO}"
    response = requests.get(url).json()
    feels_like = response['main']['feels_like']
    temp_min = response['main']['temp_min']
    temp_max= response['main']['temp_max']

    sunrise = response['sys']['sunrise']
    sunrise = pd.Timestamp(sunrise, unit='s', tz=response['timezone']) 
    sunrise = sunrise.strftime('%Y-%m-%d %X')

    sunset = response['sys']['sunset']
    sunset = pd.Timestamp(sunset, unit='s', tz=response['timezone']) 
    sunset = sunset.strftime('%Y-%m-%d %X')
    

    new_line='</br>'
    profile = (

        #f"response: {response} {new_line} {new_line}"
        f"<h1>City: {CITY_NAME} </h1>{new_line}"
        f"Feels Like: {round( (feels_like - 273.15) * (9/5) + 32, 2)} F {new_line}"
        f"Weather: {response['weather'][0]['main']} {new_line}"
        f"Description: {response['weather'][0]['description']} {new_line}"
        f"Sunrise: {sunrise} {new_line}"
        f"Sunset: {sunset} {new_line}"
        f"Min Temp: {round( (temp_min - 273.15) * (9/5) + 32, 2)} F {new_line}"
        f"Max Temp: {round( (temp_max - 273.15) * (9/5) + 32, 2)} F{new_line}"
        f"Country: {response['sys']['country']} {new_line}"
        f"lon/lat: {response['coord']} {new_line}"
        

         
    )
   
    return profile

# def him(response):
#     return f"THIS IS 2nd line: {response}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


