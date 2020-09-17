from rest_framework import serializers
import datetime
class WeatherDataSerilizer(serializers.Serializer):

   coord = serializers.DictField(child=serializers.CharField())
   weather = serializers.ListField(child=serializers.DictField(child=serializers.CharField()))
   base = serializers.CharField()
   main = serializers.DictField(child=serializers.CharField())
   visibility =  serializers.CharField()
   wind = serializers.DictField(child=serializers.CharField())
   clouds = serializers.DictField(child=serializers.CharField())
   dt =  serializers.CharField()
   sys = serializers.DictField(child=serializers.CharField())
   timezone = serializers.CharField()
   name = serializers.CharField()
   cod = serializers.CharField()

class DetailsSerilizer(serializers.Serializer):
	city = serializers.CharField()