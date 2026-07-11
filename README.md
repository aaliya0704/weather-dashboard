# weather-dashboard
A professional Python-based Weather Dashboard application that fetches real-time weather data using the OpenWeather API.

## Features
- Fetches real-time weather data using the OpenWeather API.
- Displays the city name.
- Displays the current temperature in Celsius.
- Displays the humidity percentage.
- Displays the weather description.
- Handles invalid city names gracefully.
- Handles network connection failures using exception handling.
- Includes automated unit tests using pytest.
- Uses environment variables to securely store API keys.
- Implements logging for application events.
- Organized using a professional modular project structure.

## Technologies Used
| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Requests | Communicates with the OpenWeather API |
| OpenWeather API | Provides live weather data |
| python-dotenv | Loads environment variables from the `.env` file |
| Pytest | Automated unit testing |
| Logging | Records application events and errors |
| Git & GitHub | Version control and project hosting |

## Project Structure
```text
weather-dashboard/
│
├── src/
│   ├── main.py
│   ├── weather.py
│   ├── config.py
│   └── logger.py
│
├── tests/
│   └── test_weather.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/<your-github-username>/weather-dashboard.git
```

2. Navigate to the project directory

```bash
cd weather-dashboard
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate.bat
```

5. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

This project uses environment variables to securely store sensitive information such as the OpenWeather API key.

1. Create a `.env` file in the project root.

2. Copy the contents of `.env.example` into the `.env` file.

3. Replace the placeholder value with your own OpenWeather API key.

Example:

```env
WEATHER_API_KEY=your_api_key_here
```

> **Note:** Never commit your `.env` file to GitHub. Only commit `.env.example`.

## Running the Application

To start the Weather Dashboard, run:

```bash
python src/main.py
```

The application will prompt you to enter a city name.

Example:

```text
Enter city name: Mumbai

City: Mumbai
Temperature: 29.3 °C
Humidity: 76%
Weather: Overcast Clouds
```

## Running Tests

This project uses **pytest** for automated unit testing.

To run all tests, execute:

```bash
pytest
```

To display console output while running the tests, execute:

```bash
pytest -s
```

A successful test run will display output similar to:

```text
======================== test session starts ========================

collected 5 items

tests/test_weather.py .....                        [100%]

========================= 5 passed =========================
```