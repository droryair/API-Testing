# API-Testing
### Weather App: 

A simple Node.js application that fetches weather data from a public API using Axios and serves it via an Express server.

### API Testing: 

Using Python's unittest for writing tests and requests-mock for mocking API calls to test the application's response.
___
## Getting started

1) Create an API key from [OpenWeatherMap](https://openweathermap.org/api).

2) Go to [weather-app](weather-app), or, run from the main project directory: `cd ./weather-app`.

3) Create an `.env` file, or, run: `touch .env`.

4) Put your API Key in the `.env` file:
   ```.env
   API_KEY=<your-api-key>
   ```

   * replace `<your_api_key>` with your actual key.
   
   * __Do not__ put quotetion marks around the key.

  ### Run the wheather app:

   1. From the [weather-app](weather-app) directory, run `node index.js`.
     
   3. To ensure the app is running properly, visit: [http://localhost:3000/weather?city=London](http://localhost:3000/weather?city=London).

### Run the test:
