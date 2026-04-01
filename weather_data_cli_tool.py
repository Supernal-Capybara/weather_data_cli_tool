
import requests

def get_coords(city_input):
    location_coords = f"https://geocoding-api.open-meteo.com/v1/search?name={city_input}"
    
    try:
        response = requests.get(location_coords, timeout=5)
        response.raise_for_status()
        
    except requests.RequestException:
        print("Error retrieving data from API")
        return
    
    data = response.json()
    if "results" not in data or not data["results"]:
        print("City not found")
        return
        
    first_result = data["results"][0]
    city = first_result.get("name")
    lat = first_result.get("latitude")
    lon = first_result.get("longitude")
    
    return city, lat, lon

def retrieve_weather(lat, lon):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(weather_url, timeout=5)
        response.raise_for_status()
        weather_report = response.json()

    except requests.RequestException:
        print("Error retrieving data from API.")
        return
    
    return weather_report

def print_weather_report(city, weather_report):
    current = weather_report.get("current_weather", {})
    if not current:
        print("Weather data unavailable")
        return 

    print(f"\nWeather for {city}")
    temperature = current.get("temperature")
    print(f"Temperature: {temperature}°C")

    windspeed = current.get("windspeed")
    print(f"Wind Speed: {windspeed} km/h")

    weather_code = current.get("weathercode")
    print(f"Weather code: {weather_code}\n")
   

if __name__ == "__main__":
    while True:
        print("Welcome to the Weather Report")
        city_input = input("Please enter a city (or 'q' to quit): ").strip()
        if city_input.lower() == "q":
            print("Goodbye")
            break
        
        coords = get_coords(city_input)
        if coords is None:
            continue
        city, lat, lon = coords
        
        weather_report = retrieve_weather(lat, lon)
        if weather_report is None:
            continue
        
        print_weather_report(city, weather_report)
        
        