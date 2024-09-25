import requests

# Your WeatherAPI key
API_KEY = 'da726ca2557344169ab80242242509'
BASE_URL = "http://api.weatherapi.com/v1/current.json"


# Function to fetch weather data for a location
def get_weather_data(city_name):
    try:
        # Make an API request
        params = {'key': API_KEY, 'q': city_name}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if 'error' in data:
            return f"Error: {data['error']['message']}"

        # Extracting necessary information
        current = data['current']
        location = data['location']
        temperature = current['temp_c']
        humidity = current['humidity']
        weather_description = current['condition']['text']

        # Returning formatted weather data
        return (f"City: {location['name']}\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Weather: {weather_description.capitalize()}\n")

    except Exception as e:
        return f"An error occurred: {e}"


# Function to handle multiple locations
def weather_app():
    print("Enter city names (comma-separated) to get the weather or type 'exit' to quit.")

    while True:
        user_input = input("\nCities: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting the app.")
            break

        city_list = user_input.split(',')
        for city in city_list:
            city = city.strip()
            if city:
                weather_info = get_weather_data(city)
                print(weather_info)


# Start the application
if __name__ == '__main__':
    weather_app()


