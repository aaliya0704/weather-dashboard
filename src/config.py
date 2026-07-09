import os
# OS module lets python interact with the operating system including reading environment variables

from dotenv import load_dotenv
# This imports the load_dotenv() function from the python_dotenv library.

load_dotenv()
# This reads your .env file and loads the environment variables from .env into the program's environment.

# Reading the API keyfrom the memory and storing it in API_KEY variable
API_KEY = os.getenv("WEATHER_API_KEY")

# config.py finishes execution.
# Python returns to main.py with API_KEY now available
