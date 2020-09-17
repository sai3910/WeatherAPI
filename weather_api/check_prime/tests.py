from django.test import TestCase
from django.test import Client

class ViewsDataTestCase(TestCase):
	def test_data_loads_properly(self):
		c = Client()
		response = c.post('/check_prime/check_weather/', {'city': 'Hyderabad'})
		self.assertEqual(response.status_code, 200)

	def test_get_loads_properly(self):
		c = Client()
		response = c.get('/check_prime/check_weather/')
		self.assertEqual(response.status_code, 200)

class DataFailTestCase(TestCase):
	def test_data_loads_improperly(self):
		c = Client()
		response = c.post('/check_prime/check_weather/', {})
		self.assertEqual(response.status_code, 400)
