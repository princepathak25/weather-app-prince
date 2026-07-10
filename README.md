# Weather CLI App
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenWeather API](https://img.shields.io/badge/OpenWeather_API-FFB400?style=for-the-badge&logo=openweathermap&logoColor=white)

A terminal-based weather fetching application. 
It fetches real-time weather data using the OpenWeatherMap API and wraps it in an elegant user experience.  

---

## Features

- Get weather by city name instantly
- Handles invalid input & API issues
- API key integration with ease
- Uses `time.sleep()` for a smoother flow
- Runs in a loop for multiple queries

---

## Sample Interaction

```bash
Welcome to Weather CLI App!

Enter city name (or type 'exit' to quit): Delhi
🔎 Fetching weather data...

✅ Data fetched successfully!

📍 Location: Delhi, IN
🌡️ Temperature: 34°C
☁️ Condition: Clear
💧 Humidity: 48%
🌬️ Wind Speed: 3.5 m/s
```

---

## How to Run

```bash
git clone https://github.com/princepathak25/weather-app-cli.git
cd weather-app-cli
python weather-app-prince.py
```

---

## Environment Setup

This project uses the OpenWeatherMap API.

For security reasons, the API key is not included in the repository.

### Steps to run the project:

1. Create a `.env` file in the root directory
2. Add your API key inside it:

```env
OPENWEATHER_API_KEY=your_api_key_here


---

## Setup Instructions
  
2. Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)  
3. Replace `"YOUR_API_KEY_HERE"` in the script with your actual key

```python
api_key = "your_actual_api_key"
```

---

## Project Structure

```
weather-app-cli
 ┣ weather-app-prince.py
 ┗ README.md
```

---

## Author 

**Prince Pathak**
