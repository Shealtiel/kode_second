from flask import Flask, request
from flask_caching import Cache
import requests, json


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@cache.memoize(timeout=1800)
def get_weather_from_owm(city):
    api_key = '' # Your 32-digit api-key
    url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'q': city, 'appid': api_key, 'units': 'metric'}
    owm_json = requests.get(url, params=payload).json()
    kode_json = json.dumps({'Temperature':owm_json['main']['temp'], 
                            'Pressure':owm_json['main']['pressure'] * 0.75006375541921,
                            'Wind speed':owm_json['wind']['speed']})
    return kode_json


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', '')
    return get_weather_from_owm(city)


if __name__ == '__main__':
    app.run(debug=False)
