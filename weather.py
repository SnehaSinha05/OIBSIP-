import requests

city_name = input("Enter the city: ")
api_key = "86002db922a90c13874a56f8c4f17337"
weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
response = requests.get(weather_url)
weather = response.json()

if weather.get('code')== 404:
    print( "City not found, try again!")
else:
    weather_main = weather['weather'][0]['main']
    temp = weather['main']['temp'] -273.15
    feels_like = weather['main']['feels_like'] -273.15  
    humidity = weather['main']['humidity']
    max_temp = weather['main']['temp_max']  -273.15
    min_temp = weather['main']['temp_min'] -273.15

    print(f"weather: {weather_main}")
    print(f"Temperature: {temp: .2f} °C")
    print(f"Feels like: {feels_like: .2f} °C")
    print(f"Humidity: {humidity} %")
    print(f"Max temperature: {max_temp: .2f} °C")
    print(f"Min temperature: {min_temp: .2f} °C")