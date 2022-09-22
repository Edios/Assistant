import os
from Strava import StravaClientData, StravaAuthorification
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
    print(bikes_info)

    #Strava part:
    #Show name and kilometers of bike. Plan new service info +100 km



    #Sum up kilometers


