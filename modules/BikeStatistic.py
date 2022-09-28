from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta

from Utils import send_get_request


@dataclass
class RideStatistic:
    ride_count: int
    summary_distance: int  # kilometers
    elapsed_time: int  # minutes

    def __str__(self) -> str:
        return f'Rides count: {self.ride_count}\nSummary distance: {self.summary_distance} kilometers.\nElapsed time: {self.elapsed_time} minutes. '


@dataclass
class BikeStatistics:
    strava_token: str

    def __str__(self):
        return self.__dict__

    #TODO: Return object similar to Stats
    def get_total_athlete_statistics(self, athlete_id):
        send_get_request(f'https://www.strava.com/api/v3//athletes/{athlete_id}/stats', bearer_token=self.strava_token)

    def get_statistic_between_range(self, before_date, after_date) -> RideStatistic:
        data = send_get_request(
            f'https://www.strava.com/api/v3/athlete/activities?before={before_date}&after={after_date}&per_page=50',
            bearer_token=self.strava_token)
        ride_count = len(data)
        summary_distance = sum([int(single_ride['distance'] * 0.001) for single_ride in data])
        elapsed_time = sum([int(single_ride['elapsed_time']) // 60 for single_ride in data])
        stats = RideStatistic(ride_count, summary_distance, elapsed_time)
        return stats

    # TODO: Remove redundant method - this could be simplified
    def get_today_statistics(self):
        after_date = datetime.now() - relativedelta(hours=24)
        before_date = datetime.now()
        stats = self.get_statistic_between_range(before_date.timestamp(), after_date.timestamp())
        return stats

    def get_weekly_statistics(self):
        after_date = datetime.now() - relativedelta(weeks=1)
        before_date = datetime.now()
        stats = self.get_statistic_between_range(before_date.timestamp(), after_date.timestamp())
        return stats

    def get_monthly_statistics(self):
        after_date = datetime.now() - relativedelta(months=1)
        before_date = datetime.now()
        stats = self.get_statistic_between_range(before_date.timestamp(), after_date.timestamp())
        return stats
