# Weather Data CLI Tool

This is a CLI tool that fetches real-time weather data using the Open-Meteo API.
It is designed as a simple internal-style utility for quickly retrieving weather information without using a browser or subscription service.

Features
* Accepts user input for a city name
* Uses a geocoding API to retrieve latitude and longitude
* Fetches current weather data from the Open-Meteo API
* Parses and displays temperature, wind speed, and weather conditions
* Handles invalid city input and API errors gracefully
* No API key or subscription required

Technologies Used
* Python
* Requests
* Open-Meteo API (geocoding and weather)

How to Run
* Run the file: `weather_data_cli_tool.py`
* Enter a city name when prompted
* View the weather data printed in the terminal

Requirements
* Python installed
* Requests library installed
* Internet connection (to access Open-Meteo API)

Skills Demonstrated
* Integrating multiple APIs (geocoding and weather)
* Handling API responses and parsing JSON data
* Implementing safe traversal of nested data structures
* Building a CLI tool with input validation and error handling
* Using the Requests library to perform HTTP requests

Upcoming features
* Right now the program selects the most relevant result from the API (e.g., it will choose London, UK, over London, Ontario). A future version could present multiple matching cities and allow the user to select the correct one.
* Option to display temperature in Celsius or Fahrenheit.
* Convert weather codes into human-readable descriptions (e.g., clear, cloudy, rain)