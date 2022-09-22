from dataclasses import dataclass, field
from pathlib import Path
from typing import Union

from Utils import send_get_request, read_user_data_from_json, USER_DATA_FOLDER, BIKE_SERVICE_INFO_FILENAME, \
    save_user_data_to_json


@dataclass
class Bike:
    name: str
    distance: float
    next_service: Union[None,float] = None

    def __post_init__(self):
        if not self.next_service:
            self.next_service=self.distance+100

@dataclass
class BikeAssistant:
    strava_token: str

    def get_bikes_data(self) -> list[Bike]:
        request = send_get_request(url='https://www.strava.com/api/v3/athlete', bearer_token=self.strava_token)
        bikes = [Bike(bike['name'], bike['converted_distance']) for bike in request['bikes']]
        return bikes

    def bikes_service_info(self):
        #TODO: Find better way to determine correct distance
        strava_bike_info = self.get_bikes_data()
        # Get last known service info from json
        final_bike_service_info = []

        if Path(USER_DATA_FOLDER / BIKE_SERVICE_INFO_FILENAME).exists():
            file_info = read_user_data_from_json(BIKE_SERVICE_INFO_FILENAME)
            file_bike_info = [Bike(**bike) for bike in file_info]

            for file_bike, strava_bike in zip(file_bike_info, strava_bike_info):
                if file_bike.next_service > float(strava_bike.distance + 90):
                    final_bike_service_info.append(file_bike)
                else:
                    final_bike_service_info.append(strava_bike)
        else:
            final_bike_service_info=strava_bike_info

        save_user_data_to_json(BIKE_SERVICE_INFO_FILENAME,[bike.__dict__ for bike in final_bike_service_info])



        # if no data, then self.next_service = distance+100
        # if data expired - passed 200 km then self.next_service = distance+100
        # if service info in range(distance-200,distance+90) then json data=self.next.service

        # Save actual data to json
