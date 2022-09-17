"""
#Assistant get data from DTO
Initialized by: Command(**data)
"""
import enum
from dataclasses import dataclass


@dataclass
class Keys:
    strava_api_key: str
    google_api_key: str


class BikeAssistant:
    strava_api_key: str

    def __init__(self, strava_api_key):
        self.strava_api_key = strava_api_key

    @classmethod
    def getAllStats(cls) -> dict:
        pass


class Display(enum.Enum):
    text='text'

    def print_message(self):
        pass


class Assistant:
    personalData: dict
    keys: Keys
    display: Display

    @staticmethod
    def runCommand(display:, data:dict):
        # Wrap running module
        pass

    def runStravaModule(self):
        # Send request to recive data from strava api
        # Use interface to display it to console as full sentence
        bike_assistant = BikeAssistant(self.keys.strava_api_key)
        # bike_stats= BikeAssistant.getAllStats()
        self.runCommand(display=self.display, data=bike_assistant.getAllStats())
        pass

    def fillConfig(self):
        # check for api keys in env var
        # Fill config
        pass

if __name__ == '__main__':
    assistant=Assistant()
    assistant.runStravaModule()