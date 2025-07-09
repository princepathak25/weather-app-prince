# 🌦️ Prince's Weather CLI App
# Get real-time weather with clean, emoji-driven output!

import requests
import time

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data, city):
    print("\n🌐 Weather Report:")
    print(f"📍 Location: {city.title()}")
    print(f"🌡️ Temperature: {data['main']['temp']}°C")
    print(f"🤒 Feels Like: {data['main']['feels_like']}°C")
    print(f"💧 Humidity: {data['main']['humidity']}%")
    print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
    print(f"🌤️ Condition: {data['weather'][0]['description'].title()}")
    print("✅ Data fetched successfully!\n")
    time.sleep(2)

def main():
    print("🌦️ Welcome to Prince Pathak's Weather CLI App!\n")
    api_key = "d475a2f672cd89541a5c625847609086"  # Replace with your actual API key

    while True:
        city = input("🏙️ Enter city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("\n👋 Thanks for using Prince’s Weather App. Stay warm (or cool)!")
            break

        print("🔍 Fetching weather data...\n")
        time.sleep(1.5)

        data = get_weather(city, api_key)
        if data:
            display_weather(data, city)
        else:
            print("❌ City not found or API issue. Try again.\n")

if __name__ == "__main__":
    main()
# End of the weather app code
# Enjoy staying updated with the weather! 🌤️🌧️
