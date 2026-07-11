from unittest.mock import patch
from requests.exceptions import RequestException
# AUTOMATED TEST CODE:
# The purpose of this test is to automatically verify that get_weather() works correctly.
# Inshort: pytest calls the get_weather() -> receives the returned dictionary -> verifies that the dictionary is correct.


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
    # pytest runs test_get_weather() function -> python calls get_weather() in weather.py with a custom city value to test if the function works with that value -> python leaves test_weather.py and jumps to weather.py -> the execution continues there -> url is created -> request library takes the url and sends an http get request to the weather API Server -> this server fetches the relevat data from the Weather Database and generates a JSON response.
    # The request library receives the json response -> request library creates a response object which converts the json response into a python dictionary using the json() method -> This python dictionary is then stored in the variable weather_data -> the dictionary is returned to test_get_weather() which called for it -> it is then stored inside the weather_data variable.

    # ADDING ASSERTIONS:----------------------------------------------------------------
    assert weather_data is not None
    # the main responsibility of get_weather() is to return the weather dictionary -> incase if something is wrong with the function it will return "None" meaning the function has failed.
    # therefore, the above assertion checks if the value returned by the function is not None.
    # even if the seertion return something that is not what you requested for, still the test will pass. Due to this we are using more assertions.
    assert weather_data["name"] == "Mumbai"
    # This assertion verifies if the user gets the weather for the city they have requested.

    assert "main" in weather_data
    # This assertion verifies that the dictionary contains the main section, because before accessing a key we first should check whether that key actually exists in the dictionary

    assert "temp" in weather_data["main"]
    # This assertion verifies if temp or temperature exists inside the nested dictionary main

    assert isinstance(weather_data["main"]["temp"], (int, float))
    # isinstance(value, datatypes) -> always checks whether a value belongs to particular datatypes

    assert "description" in weather_data["weather"][0]

    assert isinstance(weather_data["weather"][0]["description"], str)


def test_invalid_city():
    weather_data = get_weather("abcdefghijk")
    assert weather_data is None
    # This assertion verifies that when an invalid city is entered, the value returned by the function is None


# ------------------------FAKE TEST---------------------------
@patch("src.weather.requests.get")
# This lientells python to temporarily replace the real request.get() inside src.weather with a fake one.
# So python replaces the  request.get() (because it is what communicates with weather API) with mock_get
def test_network_failure(mock_get):
    # patch creates a mock object "mock_get" for you and passes it as the 1st argument to your test function
    # Usually after receiving a JSON response from the Weather database, a response object is created, but because of @patch, python has secretly replaced request.get with mock_get. This way the code is doing this:
    # response = mock_get(url) INSTEAD OF response = requests.get(url) and the real request.get() is never called -> THIS RAISES AN REQUESTEXCEPTION

    # Now we will tell the mock to raise an exception as:
    mock_get.side_effect = RequestException
    # Now whenever mock_get() is called, it raises a  RequestException
    # Now whne the test function calles get_weather() as below, python jumps into weather.py and the execution starts from response = requests.get(url) -> now because of @patch, python has replaced that requests.get() with mock_get() -> this mock_get() brings the program back to the test and immediately raises a RequestException and python jumps back to except RequestException: block of weather.py and executes it and returns None and program comes back to the test -> Since it returns None it matches with the assertion of weather_data == None, this evaluates to true
    weather_data = get_weather("Mumbai")
    assert weather_data is None
