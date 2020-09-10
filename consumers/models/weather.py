"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        if message.topic() == 'org.chicago.cta.weather.v1':
            weather_info = message.value()
            self.temperature = weather_info['temperature']
            self.status = weather_info['status']
            logger.debug(
                "received weather data from kafka, temp: %s, status: %s",
                self.temperature,
                self.status,
            )
