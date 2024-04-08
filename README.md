# mars-weather-reporter

The Mars InSight Weather API provides access to Mars’ atmospheric data collected by NASA’s InSight lander. This data includes information about temperature, wind speed, wind direction, and atmospheric pressure on the Martian surface.

# Available Data
The API provides the following data:

1) Sol Number: Mars days are called “sols.” The API allows you to query data for a specific sol.
2) Atmospheric Temperature: The temperature on Mars’ surface.
3) Horizontal Wind Speed: The speed of horizontal winds.
4) Atmospheric Pressure: The atmospheric pressure at the landing site.
5) Wind Direction: The direction of the wind.

# Why We Don’t Get Data Anymore
Unfortunately, as of now, the Mars InSight Weather API is no longer providing real-time data. The last update was in 2020. Due to technical issues or other factors, NASA has discontinued regular updates. Therefore, the data retrieved from the API may not reflect the current Martian weather conditions. This application just fetches the deserialized JSON data the API provides. 