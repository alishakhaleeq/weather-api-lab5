from weather_api import WeatherAPI
from datetime import datetime

class PersonalWeatherStation:
    def __init__(self):
        self.api = WeatherAPI()
        self.current_city = None
        self.current_coords = None
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("       Personal Weather Station")
        print("="*50)
        print("1. Set Location")
        print("2. Current Weather")
        print("3. Weekly Forecast")
        print("4. Hourly Timeline (24 hours)")
        print("5. Compare Cities")
        print("6. Weather History") 
        print("7. Exit")
        print("="*50)
    
    def set_location(self):
        """Set the current location"""
        city = input("Enter city name: ").strip()
        if city:
            print(f"Looking up coordinates for {city}...")
            lat, lon, found_city = self.api.get_coordinates(city)
            if lat and lon:
                self.current_coords = (lat, lon)
                self.current_city = found_city
                print(f"Location set to: {found_city}")
                print(f"Coordinates: {lat:.2f}, {lon:.2f}")
            else:
                print("City not found. Please try again.")
        else:
            print("Please enter a valid city name.")
    
    def show_current_weather(self):
        """Display current weather conditions"""
        if not self.current_coords:
            print("Please set a location first (option 1).")
            return
        
        print(f"\nFetching current weather for {self.current_city}...")
        data = self.api.get_current_weather(self.current_coords[0], self.current_coords[1])
        
        if data and 'current' in data:
            current = data['current']
            print(f"\n--- Current Weather in {self.current_city} ---")
            print(f"Time: {current.get('time', 'N/A')}")
            print(f"Temperature: {current.get('temperature_2m', 'N/A')}°C")
            print(f"Humidity: {current.get('relative_humidity_2m', 'N/A')}%")
            print(f"Wind Speed: {current.get('wind_speed_10m', 'N/A')} km/h")
            print(f"Wind Direction: {current.get('wind_direction_10m', 'N/A')}°")
            
            weather_code = current.get('weather_code')
            if weather_code is not None:
                description = self.api.get_weather_code_description(weather_code)
                print(f"Conditions: {description}")
        else:
            print("Unable to fetch current weather data.")
    
    def show_weekly_forecast(self):
        """Display 7-day weather forecast"""
        if not self.current_coords:
            print("Please set a location first (option 1).")
            return
        
        print(f"\nFetching weekly forecast for {self.current_city}...")
        data = self.api.get_weekly_forecast(self.current_coords[0], self.current_coords[1])
        
        if data and 'daily' in data:
            daily = data['daily']
            print(f"\n--- 7-Day Forecast for {self.current_city} ---")
            
            for i, date in enumerate(daily['time']):
                print(f"\n{date}:")
                print(f"  High: {daily['temperature_2m_max'][i]}°C")
                print(f"  Low: {daily['temperature_2m_min'][i]}°C")
                print(f"  Precipitation: {daily['precipitation_sum'][i]}mm")
                print(f"  Max Wind: {daily['wind_speed_10m_max'][i]}km/h")
                
                weather_code = daily['weather_code'][i]
                description = self.api.get_weather_code_description(weather_code)
                print(f"  Conditions: {description}")
        else:
            print("Unable to fetch weekly forecast data.")
    
    def show_hourly_timeline(self):
        """Display 24-hour weather timeline"""
        if not self.current_coords:
            print("Please set a location first (option 1).")
            return
        
        print(f"\nFetching hourly timeline for {self.current_city}...")
        data = self.api.get_hourly_forecast(self.current_coords[0], self.current_coords[1], 24)
        
        if data and 'hourly' in data:
            hourly = data['hourly']
            print(f"\n--- 24-Hour Timeline for {self.current_city} ---")
            
            for i, time in enumerate(hourly['time'][:24]):  # Show first 24 hours
                dt = datetime.fromisoformat(time.replace('T', ' '))
                print(f"{dt.strftime('%H:%M')}: {hourly['temperature_2m'][i]}°C, "
                      f"Humidity: {hourly['relative_humidity_2m'][i]}%")
        else:
            print("Unable to fetch hourly timeline data.")
    
    def compare_cities(self):
        """Compare weather between two cities"""
        print("\n--- City Weather Comparison ---")
        
        # Get first city
        city1 = input("Enter first city: ").strip()
        if not city1:
            print("Invalid city name.")
            return
            
        lat1, lon1, name1 = self.api.get_coordinates(city1)
        if not lat1:
            print(f"Could not find {city1}")
            return
        
        # Get second city
        city2 = input("Enter second city: ").strip()
        if not city2:
            print("Invalid city name.")
            return
            
        lat2, lon2, name2 = self.api.get_coordinates(city2)
        if not lat2:
            print(f"Could not find {city2}")
            return
        
        # Get weather for both cities
        weather1 = self.api.get_current_weather(lat1, lon1)
        weather2 = self.api.get_current_weather(lat2, lon2)
        
        if weather1 and weather2:
            print(f"\n{name1:^25} | {name2:^25}")
            print("-" * 53)
            
            temp1 = weather1['current'].get('temperature_2m', 'N/A')
            temp2 = weather2['current'].get('temperature_2m', 'N/A')
            print(f"Temperature: {temp1:>8}°C      | {temp2:>8}°C")
            
            hum1 = weather1['current'].get('relative_humidity_2m', 'N/A')
            hum2 = weather2['current'].get('relative_humidity_2m', 'N/A')
            print(f"Humidity:    {hum1:>8}%       | {hum2:>8}%")
            
            wind1 = weather1['current'].get('wind_speed_10m', 'N/A')
            wind2 = weather2['current'].get('wind_speed_10m', 'N/A')
            print(f"Wind Speed:  {wind1:>8}km/h    | {wind2:>8}km/h")
        else:
            print("Unable to fetch comparison data.")
    
    def weather_history_placeholder(self):
        """Placeholder for weather history feature"""
        print("\n--- Weather History ---")
        print("This feature would show historical weather data.")
        print("Implementation requires historical weather API endpoints.")
        print("(This is a placeholder - you can expand this feature)")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Personal Weather Station!")
        print("Powered by Open-Meteo API")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nSelect an option (1-7): ").strip()
                
                if choice == '1':
                    self.set_location()
                elif choice == '2':
                    self.show_current_weather()
                elif choice == '3':
                    self.show_weekly_forecast()
                elif choice == '4':
                    self.show_hourly_timeline()
                elif choice == '5':
                    self.compare_cities()
                elif choice == '6':
                    self.weather_history_placeholder()
                elif choice == '7':
                    print("\nThank you for using Personal Weather Station!")
                    print("Goodbye! 🌤️")
                    break
                else:
                    print("Invalid option. Please select 1-7.")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye! 🌤️")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                print("Please try again.")

if __name__ == "__main__":
    # Install required package if not already installed
    try:
        import requests
    except ImportError:
        print("Installing required packages...")
        import subprocess
        subprocess.check_call(["pip", "install", "requests"])
        import requests
    
    # Run the application
    app = PersonalWeatherStation()
    app.run()