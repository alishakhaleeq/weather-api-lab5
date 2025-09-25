import requests
import json
from datetime import datetime, timedelta

class WeatherAPI:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    
    def get_coordinates(self, city_name):
        """Get latitude and longitude for a city name"""
        try:
            params = {
                'name': city_name,
                'count': 1,
                'language': 'en',
                'format': 'json'
            }
            response = requests.get(self.geocoding_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data['results']:
                result = data['results'][0]
                return result['latitude'], result['longitude'], result['name']
            else:
                return None, None, None
        except requests.RequestException as e:
            print(f"Error getting coordinates: {e}")
            return None, None, None
    
    def get_current_weather(self, latitude, longitude):
        """Get current weather conditions"""
        try:
            params = {
                'latitude': latitude,
                'longitude': longitude,
                'current': ['temperature_2m', 'relative_humidity_2m', 'weather_code', 
                           'wind_speed_10m', 'wind_direction_10m'],
                'timezone': 'auto'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting current weather: {e}")
            return None
    
    def get_weekly_forecast(self, latitude, longitude):
        """Get 7-day weather forecast"""
        try:
            params = {
                'latitude': latitude,
                'longitude': longitude,
                'daily': ['temperature_2m_max', 'temperature_2m_min', 'weather_code',
                         'precipitation_sum', 'wind_speed_10m_max'],
                'timezone': 'auto',
                'forecast_days': 7
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting weekly forecast: {e}")
            return None
    
    def get_hourly_forecast(self, latitude, longitude, hours=24):
        """Get hourly forecast"""
        try:
            params = {
                'latitude': latitude,
                'longitude': longitude,
                'hourly': ['temperature_2m', 'relative_humidity_2m', 'weather_code'],
                'timezone': 'auto',
                'forecast_hours': hours
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting hourly forecast: {e}")
            return None
    
    def get_weather_code_description(self, code):
        """Convert weather codes to descriptions"""
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog",
            51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
            71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
            95: "Thunderstorm", 96: "Thunderstorm with hail"
        }
        return weather_codes.get(code, f"Unknown weather code: {code}")