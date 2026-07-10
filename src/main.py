from logger import logger
import weather  # now we have made the weather.py mosule available, but it does not fetch the weather data yet.


def main():
    logger.info("Weather Dashboard started.")
    city = input("Enter city name: ")  # the user input has now been captured.
    # Now we will pass the city variable to weather.py by calling get_weather(city) function as:
    weather_data = weather.get_weather(
        city
    )  # This calls the get_weather() from weather.py
    # Now main.py has received the weather_data dictionary from weather.py and the dictionary has been stored in weather_data variable.

    # print("City: ", weather_data["main"])  The result of this is:
    # {'temp': 29.05, 'feels_like': 35.56, 'temp_min': 29.05, 'temp_max': 29.05, 'pressure': 1006, 'humidity': 83, 'sea_level': 1006, 'grnd_level': 1005}
    if weather_data is not None:
        # With the help of this, we can specifically pick keys for City, Temperature, Humidity, and print them as:
        print(f"Showing results for {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']} Degree Celcius")
        print(f"Humidity: {weather_data['main']['humidity']} %")
        print(f"Weather: {weather_data['weather'][0]['description'].title()}")


if __name__ == "__main__":
    main()

# cod = status code:
# cod: 200 = everything is ok
