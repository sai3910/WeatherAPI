from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime


from rest_framework import views
from rest_framework.response import Response
from .serializers import WeatherDataSerilizer, DetailsSerilizer
from rest_framework import status
import requests
import json
import os

def env(var_name, default=""):
    try:
        return os.environ[var_name]
    except KeyError:
        if not default:
            error_msg = "Set the %s environment variable" % var_name
            raise AssertionError(error_msg)
        else:
            return str(default)
 

class Today_Weather(views.APIView):
	serializers_class = WeatherDataSerilizer
	def prime(self,day_today):
		if day_today>1: 
		     
			for i in range(2, day_today): 
			    
				if (day_today % i) == 0: 
					print(day_today, "is not a prime number")
					return False
				else: 
				 print(day_today, "is a prime date") 
				 return True

		else: 
		 print(day_today, "is not a prime date")
		 return False

	def get(self, request,format=None):
	
		results= {"Message":"Enter city Name"}

		return Response(results)
	def fetchData(self, city):
		BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
		CITY = city
		API_KEY = env("API_KEY")
		URL = BASE_URL+"q="+CITY+"&appid="+API_KEY
		response = requests.get(URL)
		return response

	def post(self, request):

		serializer = DetailsSerilizer(data=request.data)
		if not request.data:
			return Response({'error': "Please provide City Name"},
				status=status.HTTP_400_BAD_REQUEST)

		if serializer.is_valid():
			city = serializer.data.get('city')
			# date = serializer.data.get('date')
			date = datetime.date.today()
			
			print(city,date)
			isPrime = self.prime(17)

			if isPrime:
				
				response = self.fetchData(city)
				print(response.status_code)
				
				if response.status_code == 200:
					data = response.json()
					final_data= [{"coord": data['coord'],
									"weather": data['weather'],
									"base":data['base'],
									"main":data['main'],
									"visibility": data['visibility'],
									"wind": data['wind'],
									"clouds": data['clouds'],
									"dt": data['dt'],
									"sys": data['sys'],
									"timezone": data['timezone'],
									"name": data['name'],
									"cod": data['cod']}]
					results = WeatherDataSerilizer(final_data, many=True).data
				else:
					results = {"Error": "Request is not Succesful"}

			else :
				results= {"Error":"Date is not prime so no date"}

			return Response(results)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
