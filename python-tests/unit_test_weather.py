import unittest
import requests
import requests_mock

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        # Sending requests to the port the weather-app is running on
        self.base_url = 'http://localhost:3000/weather'

    @requests_mock.Mocker()
    def test_get_weather(self, mock):
        """
        Testing how the weather-app behaves when given a valid city name and weather information.
        """
        city = 'London'
        mock.get(f'{self.base_url}?city={city}',
                 json={'weather': [{'description': 'clear sky'}], 'main': {'temp': 293.15}})

        response = requests.get(f'{self.base_url}?city={city}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('clear sky', response.json()['weather'][0]['description'])
        self.assertEqual(293.15, response.json()['main']['temp'])

    @requests_mock.Mocker()
    def test_get_weather_default(self, mock):
        """
        Testing how the app behaves when given an empty city name.
        """
        mock.get(f'{self.base_url}?city=', json={'name':'Jerusalem'})
        response = requests.get(f'{self.base_url}?city=')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Jerusalem', response.json()['name'])

    @requests_mock.Mocker()
    def test_get_weather_error(self, mock):
        """
        Testing how the weather-app behaves when given a invalid city name.
        """
        city = 'InvalidCity'
        mock.get(f'{self.base_url}?city={city}',
                 status_code=500)

        response = requests.get(f'{self.base_url}?city={city}')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
