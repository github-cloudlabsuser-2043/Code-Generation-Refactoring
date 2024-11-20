import requests

def get_weather(city):
    api_key = "9956865bd3877ea1e4d25bcfc294802a"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)