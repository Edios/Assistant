"""
#Assistant get data from DTO
Initialized by: Command(**data)
"""
import abc
import enum
from dataclasses import dataclass


# @dataclass
# class Keys:
#     strava_api_key: str
#     google_api_key: str


# class BikeStats:
#     strava_api_key: str
#
#     def __init__(self, strava_api_key):
#         self.strava_api_key = strava_api_key
#
#     @classmethod
#     def getAllStats(cls) -> dict:
#         pass


class Display(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display_message(self, message):
        pass

    def input(self, message):
        res = input(message)
        return res


class DisplayText(Display):
    # TODO: Use curses libary: https://docs.python.org/3/howto/curses.html
    def display_message(self, message):
        print("        +======================+")
        print(message)
        print("        +======================+")


class DisplayMode(enum.Enum):
    # text=DisplayText()
    text = 'text'

    @staticmethod
    def initialize_display(mode):
        if mode == DisplayMode.text:
            return DisplayText()
        else:
            raise ValueError(f"Unknown mode: {mode}")


class Module(enum.Enum):
    BikeStatistics = "Bike Statistic"
    BikeAssistant = "Bike Assistant"

    def __str__(self):
        return


class Assistant:
    # personalData: dict
    # keys: Keys
    display: Display
    mode: DisplayMode
    modules: list[Module]

    def __init__(self, mode, modules_list):
        self.mode = mode
        self.modules = modules_list
        self.display = DisplayMode.initialize_display(self.mode)
        self.welcome_text()
        self.get_user_command()

    #
    # @staticmethod
    # def runCommand(display, data: dict):
    #     # Wrap running module
    #     pass

    # def runStravaModule(self):
    #     # Send request to recive data from strava api
    #     # Use interface to display it to console as full sentence
    #     bike_assistant = BikeStats(self.keys.strava_api_key)
    #     # bike_stats= BikeAssistant.getAllStats()
    #     self.runCommand(display=self.display, data=bike_assistant.getAllStats())
    #     pass

    # def fillConfig(self):
    #     # check for api keys in env var
    #     # Fill config
    #     pass
    def get_user_command(self):
        command = self.display.input("\nWhat module you want to use? ")
        print(command)
        # TODO: Do something with command

    def welcome_text(self):
        self.display.display_message(f"""
        Hi!
        Im your personal assistant.
        Currently there are available modules: {', '.join([module.value for module in self.modules])}
        """)
