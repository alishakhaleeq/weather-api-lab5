# Personal Weather Station

A Python application using the Open-Meteo Weather API to provide comprehensive weather information.

## Features
- Current weather checker
- Weekly forecast
- City weather comparison  
- Hourly weather timeline
- Weather history
- Weather alerts calculator

## Issues Log

### Issues Encountered:
-Issue 1: Setting up initial project structure
-Issue 2: Making first API call
-Issue 3: Parsing JSON responses
-Issue 4: Implementing user interface
-Issue 5: Testing API responses with different weather conditions
### Resolved Issues:
Issue #1: Setting up initial project structure with proper file organization 
-Problem: Need to organize code into logical modules and create proper GitHub repository
-Solution: Created weather_api.py for API interactions and weather_station.py for main application logic
-Commit: "Initial project setup with modular file structure"

Issue #2: Making first successful API call to Open-Meteo endpoints 
-Problem: Understanding API endpoint structure and required parameters
-Solution: Used requests library with proper URL formatting and parameter dictionaries
-Commit: "Add working API connection with basic weather data retrieval"

Issue #3: Parsing JSON responses and extracting relevant weather data 
-Problem: API returns complex nested JSON that needs to be parsed correctly
-Solution: Implemented proper JSON parsing with error handling for missing keys
-Commit: "Implement JSON data parsing with error handling"

Issue #4: Implementing user-friendly menu interface and navigation 
-Problem: Need intuitive menu system for users to access different features
-Solution: Created clear numbered menu with input validation and loop structure
-Commit: "Add interactive menu system with input validation"

Issue #5: Testing API responses with different weather conditions 
-Problem: Need to verify application works correctly with various weather scenarios
-Solution: Tested with multiple cities in different climates and weather conditions
-Commit: "Complete testing with diverse weather scenarios and locations"


