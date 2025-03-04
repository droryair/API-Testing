# API-Testing
### Weather App: 

A simple Node.js application that fetches weather data from a public API using Axios and serves it via an Express server.

### API Testing: 

Using Python's unittest for writing tests and requests-mock for mocking API calls to test the application's response.
___
## Getting started

1) Create an API key from [OpenWeatherMap](https://openweathermap.org/api).

2) Clone the project.

3) Go to [weather-app](weather-app), or, run from the main project directory: `cd ./weather-app`.

4) Create an `.env` file, or, run: `touch .env`.

5) Put your API Key in the `.env` file:
   ```.env
   API_KEY=<your-api-key>
   ```

   * replace `<your_api_key>` with your actual key.
   
   * __Do not__ put quotetion marks around the key.

  ## Run the Wheather App:

   1. From the [weather-app](weather-app) directory, run `node index.js`.
     
   2. To ensure the app is running properly, visit: [http://localhost:3000/weather?city=London](http://localhost:3000/weather?city=London), expecting a valid json response.

## Run the Tests:

> [!IMPORTANT]
> The weather-app must run in the backround for the tests to execute successfully.
> 
> Do not close the weather-app terminal or stop its process.
   
   1. While the weather-app is running, go to [python-tests](python-tests).
   
   2.   Open a new terminal.

         2.1. For unit tests: run: `python -m unittest unit_test_weather.py`

         2.2. For integration tests: run `python -m unittest integration_test_weather.py`

## Tests Explanation:

### Unit Tests (mocked responses):

1) test_get_weather:
   * Testing how the weather-app behaves when given a valid city name and weather information.
   * Input:
     - city = 'London'
     - weather-description = 'clear sky
     - main-temp = 293.15
   * Expected:
     - response code == 200.
     - Weather data:
       - 'clear sky' description
       - 293.15 degrees
2) test_get_weather_default:
   * Testing how the app behaves when given an empty city name.
   * Input:
     - city=''
   * Expected:
     - response code == 200.
     - city == 'Jerusalem'.
3) test_get_weather_error:
   * Testing how the weather-app behaves when given a invalid city name.
   * Input:
     - city = 'InvalidCity'
   * Expected:
     - response code == 500.

### Integration Tests (real responses):

1) test_weather
   * Testing real API request with valid city name.
   * Input:
     - city = 'London'
   * Expected:
     - response code == 200
     - city name == 'London
       
3) test_get_weather_error
   * Testing real API request with invalid city name.
   * Input:
     - city = 'InvalidCity'
   * Expected:
     - response code == 500 
   
5) test_get_weather_default
    * Testing real API request with no city name.
    * Input:
      - city = ''
    * Expected:
      - response code == 200 
      - city == 'Jerusalem'
