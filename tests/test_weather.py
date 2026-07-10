# AUTOMATED TEST CODE:


# src/ contains the actual application.
# tests/ contains programs that check whether the application works correctly.

# main.py → Application entry point (orchestrates the program).
# weather.py → Business logic (the actual work).
# test_weather.py → Verifies the business logic.

# A test is a python progra, build to check whether the exising code works.
# Testing helps you discover the bugs that you may not discover otherwise.
# FOR TESTING:
# Install pytest -> Pytest helps us run automated tests.
# Add the installed pytest package to requirements.txt using "pip freeze > requirements.txt" -> pip freeze generates the currently insattled package name -> ">" this redirection symbol writes that package directly to the requirements.txt file.

from src.weather import get_weather
# Why are we using weather.py for the text instead of main.py:
# Because get_weather() is defined inside weather.py, and we want to verify the behaviour of tat function.
# main.py is only responsible for interacting with the user for taking input and displaying the output.


def test_get_weather():  # as per the rules of pytest, it only looks for functions that start with "test....()", so pytest fucntions should always start with test....
    weather_data = get_weather("Mumbai")
    # Now the testing flow becomes:
    # pytest runs test_get_weather() function -> python calls get_weather() in weather.py with a custom city parameter -> python leaves test_weather.py and jumps to weather.py -> the execution continues there -> url is created -> request library takes the url and sends an http get request to the weather API Server -> this server fetches the relevat data from the Weather Database and generates a JSON response.
    # The request library receives the json response -> request library creates a response object which converts the json response into a python dictionary using the json() method -> This python dictionary is then stored in the variable weather_data -> the dictionary is returned to test_get_weather() which called for it -> it is then stored inside the weather_data variable.

    assert weather_data is not None
    # The assert keyword verifies that weather_data is not None and contains valid data -> returns True -> Test passed! -> SUCCESS.
