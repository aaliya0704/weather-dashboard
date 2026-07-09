# weather related function will be added here

# The program needs a request library for communicating with the Weather API:
import requests

# Now we tell the program where and what our API key is. This will make the API_KEY available.
from config import API_KEY


def get_weather(
    city,
):  # without the city parameter, the program won't know which city to display.

    # AS SOON AS THE GET_WEATHER() IS CALLED BY MAIN.PY, WEATHER.PY CREATES THE URL AS:

    # Now writing the url is like writing the address on the envelop. Before sending a request we must mention the complete address of the Weather API and store it in a "url" variable.
    # This is similar to:
    # name = "Aaliya" or total = 500.
    # The reason why the url is longer: the address is not of a website, instead it is requesting data telling the Weather API following things:
    # which service we want  -> which city we want -> which API key we are using -> whihc unite we prefer -> all of this info makes the url longer than just a website's address.
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        # Here:
        # Everything after ? tells the server what the program wants.
        # https://api.openweathermap.org  -> this is the address of the weather API server, just like www.google.com
        f"q={city}&"
        f"appid={API_KEY}&"
        f"units=metric"
        # here:
        # the city parameter tells Weather API, which city's weather data the program wants.
        # This city value travelled from main.py through the get_weather(city) and is now available inside weather.py.
        # appid -> it means the API key. We need to specify that to get access to the API.
        # This API_KEY has travelled like this:
        # from .env -> config.py -> weather.py -> API_KEY variable -> Here.
        # units=metric -> This tells the Weather API to send the temperature in Celcius, which would be sent in kelvin, if we dont write unit=metric.
    )

    response = requests.get(url)
    # Now the requests library takes the url and creates an HTTP get request.
    # This request now leaves your computer and the Weather API server on another computer receives this request.
    # The reques looks like this:
    # GET request
    # City = Mumbai
    # API Key = your_api_key
    # Units = metric

    # On receinving the request, the weather API server begins working. THer server asks itself if the API key is valid and if the city exists:
    # if yes -> it continues -> otherwise it returns an error.
    # now the weather API server goes to the weather database -> searches for Mumbai -> returns the weather of mumbai to the Weather API server.
    # Now the weather API server creates a json response -> this response is received by the requests library.
    # The requests library creates a RESPONSE OBJECT and stores it in response variable

    weather_data = response.json()
    # The response object owns a method called json() -> it converst the JSON response received by the request lobrary into a python dictionary.
    # This python dictionary is then stored in the variable weather_data.
    return weather_data
    # Now we return the weather_data dictionary to main.py from where it called get_weather()
