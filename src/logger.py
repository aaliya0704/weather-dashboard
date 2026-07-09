import logging

logging.basicConfig(  # Configuring the logging format -> pyhton uses this structure to display the logs
    level=logging.INFO,  # This tells python to show the messages whose level is INFO.
    format="%(asctime)s - %(levelname)s - %(message)s",  # This controls how every log message is displayed.
)
logger = logging.getLogger(
    __name__
)  # This creates a logger object that will be used when we write a log.

# logger.py finishes execution
# Python returns to main.py with the logger object available.
