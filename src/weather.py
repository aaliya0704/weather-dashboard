# weather related function will be added here

# The program needs a request library for communicating with the Weather API:
import requests
from requests.exceptions import RequestException
# Inside the requests library there is a mudule called requests.exceptions -> inside this module there is an exception class: RequestException.
# This class represents request-related failures.

# REQUEST-RELATED FAILURES:
# These error occur when your computer makes a request to the Weather API Servber for the weather data, but the request fails and weather API may never receive your request.
# The reques might fails due to these reasons:
# No internet connection
# Wrong website address
# Server not responding or is down.

# Which is not a request related error:
# When the reques is successfully received by the API server and it sends you the data, after this whatever error occurs is not a request related error.

# Now we tell the program where and what our API key is. This will make the API_KEY available.
from src.config import API_KEY


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

    try:  # Try to execute the following code, you don't know yet weather the code will succeed, you are just trying it.
        response = requests.get(url)
        # Now the requests library takes the url and creates an HTTP get request.
        # This request now leaves your computer and the Weather API server on another computer receives this request.
        # The reques looks like this:
        # GET request
        # City = Mumbai
        # API Key = your_api_key
        # Units = metric

        # On receinving the request, the weather API server begins working. The server asks itself if the API key is valid and if the city exists:
        # if yes -> it continues -> otherwise it returns an error.
        # now the weather API server goes to the weather database -> searches for Mumbai -> returns the weather of mumbai to the Weather API server.
        # Now the weather API server creates a json response -> this response is received by the requests library.
        # The requests library creates a RESPONSE OBJECT and stores it in response variable

        weather_data = response.json()
        # The response object owns a method called json() -> it converts the JSON response received by the request library into a python dictionary.
        # This python dictionary is then stored in the variable weather_data.

        # TEMPORARY CODE:
        print(weather_data)

        # If user types an invalid city the following if block is executed:
        if weather_data["cod"] != 200:
            print("City not found!")
            return None
        return weather_data
    # Now we return the weather_data dictionary to main.py from where it called get_weather()

    # If an error occurs with the try block, then the program jumps to the except block:
    # We will catch only the Exceptions raised by the requests library.
    except (
        RequestException
    ):  # An exception is the error that occurs while the program is running.
        print("Unable to connect to the weather API")
        print("Please check your internet connection")
        return None


#  REQUEST-RELATED ERROR EXAMPLE:
# SUPPOSE:
# Pyhton executes response = requests.get(url) -> now the reques library tries to connect with the weather API.
# If in case the internet is unavailable -> request library cannot complete the request, at this point the request library creates an exception object which belongs to the RequestException class.
# now python skips the reamining lines in the try block and immediately jumps to the except block.
# Now python verifies that the exception is of type RequestException -> if yes -> it stores that exception inside "e" -> executes this except block.
# If the exception is of wanother type and not a request-related exception -> it looks for another except matching block
