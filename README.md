# Kode Second
## Setup
### Install Python3
From https://www.python.org/
### Create virtual enviroment
```
$ cd /path/to/kode_second
$ python -m venv ./environment
$ ./kodenv/Scripts/activate
```
### Install requirements
```
$ pip install -r requirements.txt
```
### Enter your API-key
Login into your openweathermap account and get API-key [here](https://home.openweathermap.org/api_keys).
Then put it in `api_key` in ./app.py
## Launch app
```
$ python ./app.py
```
## Test it
Open browser and go to http://127.0.0.1:5000/weather?city=<city_name>  
For example: http://127.0.0.1:5000/weather?city=Kaliningrad
