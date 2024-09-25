from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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
        return {
            'city': location['name'],
            'temperature': temperature,
            'humidity': humidity,
            'weather_description': weather_description.capitalize()
        }

    except Exception as e:
        return f"An error occurred: {e}"


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city_name = request.form.get('city')
        if city_name:
            weather_data = get_weather_data(city_name)
            if isinstance(weather_data, str):  # If it's an error message
                error_message = weather_data
                weather_data = None

    return render_template('index.html', weather=weather_data, error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
