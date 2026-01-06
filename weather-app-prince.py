# 🌦️ Prince's Weather CLI App
# Get real-time weather with clean, emoji-driven output!

import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please set OPENWEATHER_API_KEY in .env file")

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def display_weather(data, city):
    print("\n🌐 Weather Report")
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

    while True:
        city = input("🏙️ Enter city name (or type 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("\n👋 Thanks for using Prince’s Weather App. Stay safe!")
            break

        if not city:
            print("⚠️ Please enter a valid city name.\n")
            continue

        print("🔍 Fetching weather data...\n")
        time.sleep(1.5)

        data = get_weather(city)
        if data:
            display_weather(data, city)
        else:
            print("❌ City not found or network issue. Try again.\n")

if __name__ == "__main__":
    main()

