import os

from modules.BikeStatistic import BikeStatistics
from modules.Strava import StravaClientData, StravaAuthorification
from modules.BikeAssistant import BikeAssistant
"""
Spawn assistant with personal info parameters
Get informations about weekly and monthly distance

Print information as full sentences

"""

if __name__ == '__main__':
    client_data2 = StravaClientData(client_id=os.getenv("API_STRAVA_CLIENT_ID"),
                                    client_secret=os.getenv('API_STRAVA_CLIENT_SECRET'),
                                    refresh_token=os.getenv('API_STRAVA_REFRESH_TOKEN'))
    auth_service2 = StravaAuthorification(client_data2)
    refresh_token = auth_service2.refresh_access_token()
    bike_assistant=BikeAssistant(auth_service2.client_data.access_token)
    #POC
    bikes=bike_assistant.get_bikes_data()
    bikes_info=bike_assistant.bikes_service_info()
    [print(single_bike) for single_bike in bikes]
    #BikeStats
    bike_stats= BikeStatistics(auth_service2.client_data.access_token)
    #athlete id: 96942628
    monthly_stats=bike_stats.get_monthly_statistics()
    weekly_stats=bike_stats.get_weekly_statistics()
    today_stats=bike_stats.get_today_statistics()
    print(monthly_stats,weekly_stats,today_stats)

    #Assistant module
    """
    Quote:
    On this {day/month/year} you totally rode {ride_count} times and it took you {elapsed_time} {"hours" if elapsed_time/60 > 1 else "minutes"}. You have traveled in total {summary_distance} kilometers.  
    """


    #Strava part:
    #Show name and kilometers of bike. Plan new service info +100 km



    #Sum up kilometers


