const express = require('express');
const axios = require('axios');
const app = express();
require('dotenv').config();

const API_KEY = process.env.API_KEY;
const BASE_URL = `https://api.openweathermap.org/data/2.5/weather`;

app.get('/weather', async (req, res) => {
  const city = req.query.city || 'Jerusalem';
  try {
    const response = await axios.get(`${BASE_URL}?q=${city}&appid=${API_KEY}`);
    res.json(response.data);
  } catch (error) {
    res.status(500).send('Error fetching weather data');
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
