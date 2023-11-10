from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '851d7e5e0791f11560c8a8811f33a526'  # Replace with your actual API key
    weather_data = get_weather_data(city, api_key)
    return render_template('weather.html', city=city, weather_data=weather_data)

def get_weather_data(city, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'imperial'}
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

if __name__ == '__main__':
    app.run
