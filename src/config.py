import os
# OS module lets python interact with the operating system including reading environment variables

from dotenv import load_dotenv
# This imports the load_dotenv() function from the python_dotenv library.

load_dotenv()
# This reads your .env file and loads its variables into the program's environment.

# Reading the API key:
API_KEY = os.getenv("WEATHER_API_KEY")
