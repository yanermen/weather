import requests
import json
from django.shortcuts import render


def weather_city(request):
    """
    :param request: We take the name of place
    :return: Get the country/city name, weather temperature(C), humidity and wind speed
    """
    if request.method == 'POST':
        place = request.POST['place']
        if place != '':
            city = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid=a105893675549eac9c5403daf671ce52'
            results = requests.get(city)
            json_data = json.loads(results.text)
            name_place = json_data['name']
            weather_temperature = int(json_data['main']['temp'] - 273.15)
            humidity = json_data['main']['humidity']
            wind_speed = json_data['wind']['speed']
            context = {
                "display": True,
                "name_place": name_place,
                "weather_temperature": weather_temperature,
                'humidity': humidity,
                "wind_speed": wind_speed,
            }
            return render(request, 'base.html', context=context)
        else:
            return render(request, 'base.html')
    else:
        return render(request, 'base.html')

