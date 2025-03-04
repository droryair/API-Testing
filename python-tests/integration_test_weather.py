import unittest
import requests

class WeatherAPITestCase(unittest.TestCase):    
    def setUp(self):
          self.base_url = " http://localhost:3000/weather"

    def test_weather(self):
        city='London'
        response = requests.get(f'{self.base_url}?city={city}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "London")

    def test_get_weather_error(self):
         city='InvalidCity'
         response= requests.get(f'{self.base_url}?city={city}')
         self.assertEqual(response.status_code, 500)

    def test_get_weather_default(self):
         city=''
         response = requests.get(f'{self.base_url}?city={city}')
         self.assertEqual(response.status_code, 200)
         self.assertEqual(response.json()["name"], 'Jerusalem')

if __name__=='__main__':
     unittest.main()
     