import requests
import json
from Speak import Bol
import geocoder
g = geocoder.ip('me')

def weathernews(ref = None):
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        if ref is not None:
            ref.gui.speaker.setText(
                "The weather is " + weather_desc['description'] + " and the temperature is " + str(
                    main['temp']) + " degree celcius. The wind speed is " + str(wind['speed']) + " m/s")
        Bol('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        Bol('weather type ' + weather_desc['main'])
        Bol('Wind speed is ' + str(wind['speed']) + ' metre per second')
        Bol('Temperature: ' + str(main['temp']) + 'degree celcius')
        Bol('Humidity is ' + str(main['humidity']))
        Bol(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        
if __name__ == '__main__':
    weathernews()