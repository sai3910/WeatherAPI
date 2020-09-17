# WeatherAPI
API which collects json data from openweathermap and sends same json when we request with a city name

## Python Version
```python 3.6.9```

## **Install Packages**
```pip install -r requirements.txt```
## **export env variables**
openweatherapikey
```export API_KEY = ""```
djangosecretkey
```export SECRET_KEY = ""``` 
## **Usage**
run server using command 

```python manage.py runserver```

## URL
enter below url
```localserver:8000/check_prime/check_weather/```
i.e. ```http://127.0.0.1:8000/check_prime/check_weather/```

### input parameter 
{"city":"CityName"}
i.e.{"city":"Hyderabad"}


