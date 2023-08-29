import requests

API_KEY = "EXAMPLE KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    print()
    data = response.json()
    weather = data['weather'][0]['description']
    print(f'Weather: {weather}')
    temperature = data['main']['temp'] * (9/5) - 459.67
    print(f'Temperature: {temperature:.1f}\u2109')
elif response.status_code == 401:
    print("\nInvalid API key.")
elif response.status_code == 404:
    print("\nUnknown city name, ZIP-code, or city ID.")
elif response.status_code == 429:
    print("\nYou have reached the limit for API calls.")
else:
    print("\nAn error has occurred.")
