import requests
import datetime

def get_public_ip():
    try:
        url = "https://api.ipify.org?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ip_address = data["ip"]
            return ip_address
        else:
            return None
    except requests.RequestException:
        return None
    
ip_address = get_public_ip()

if ip_address:
    location_data = requests.get(f"http://ip-api.com/json/{ip_address}")
    if location_data.status_code == 200:
        location_data_json = location_data.json()
        latitude = location_data_json.get("lat")
        longitude = location_data_json.get("lon")
        city = None
    else:
        city = input("Enter your location: ")
else:
    city = input("Enter your location: ")

api_key = "902674aff67d011fa4c496eb5e1ec985"

if city:
    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    )
else:
    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    )

current_time = datetime.datetime.now()

if current_time.time() < datetime.time(12, 0 ):
    greeting = "morning"
elif current_time.time() < datetime.time(17, 0):
    greeting = "afternoon"
else:
    greeting = "evening"

if weather_data.status_code == 200:
    weather_data_json = weather_data.json()

    weather_description = weather_data_json['weather'][0]['description']
    temperature = weather_data_json['main']['temp']
    weather_icon = weather_data_json['weather'][0]['icon']

    weather_icon_url = f"https://openweathermap.org/img/wn/{weather_icon}@2x.png"

    print(f"Good {greeting}! Here's your friendly weather forecast!\n")
    if weather_description == "clear sky":
        print("Today, you'll be enjoying a beautiful day with clear skies and plenty of sunshine!\n")
    elif weather_description == "light rain":
        print("Today, we're expecting light rains in the area, don't forget to grab your umbrella or bring a raincoat before heading out!\n")
    elif weather_description == "few clouds":
        print("Today, there will be a few clouds in the sky so go out and enjoy the sunshine!\n")
    else:
        print("The weather today consists of a " + weather_description + "!\n")
    
    print("The temperature today is " + str(temperature) + " °C.", end=" ")
    if temperature < 10:
        print("It's quite chilly outside, so make sure to bundle up!")
    elif temperature >= 10 and temperature < 20:
        print("The temperature is moderate, so grab a light jacket before heading out.")
    elif temperature >= 20 and temperature < 30:
        print("It's pleasantly warm today. Enjoy the outdoors!")
    elif temperature >= 30:
        print("It's a hot day, so stay hydrated and find some shade if you can.\n")
    input("Press any key to exit...")
else:
    print("Failed to retrieve weather data.\n")
    input("Press any key to exit...")