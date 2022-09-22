from dataclasses import dataclass, field
from typing import Union
from Utils import send_post_request, save_user_data_to_json


@dataclass
class StravaClientData:
    client_id: str
    client_secret: str
    code: Union[None,str] = None
    refresh_token: Union[None,str] = None
    access_token: str = field(init=False)

    def __str__(self):
        return self.__dict__


@dataclass
class StravaAuthorification:
    client_data:StravaClientData
    url = 'https://www.strava.com/oauth/token'
    # TODO: Move to other obj
    def get_auth_code(self) -> str:

        data={
            'client_id': f'{self.client_data.client_id}',
            'client_secret': f'{self.client_data.client_secret}',
            'code': {self.client_data.code},
            'grant_type': 'authorization_code'
        }

        strava_tokens = send_post_request(self.url, data)
        if "message" in strava_tokens.keys:
            raise Exception(f'Error occured, check for envirorment variables. \n Response: \n {strava_tokens["message"]}\n{strava_tokens["errors"]}')

        save_user_data_to_json('strava_client_data.json', strava_tokens)
        self.client_data.access_token = strava_tokens['access_token']
        self.client_data.refresh_token = strava_tokens['refresh_token']
        return self.client_data.access_token

    def refresh_access_token(self)->str:
        if self.client_data.refresh_token is None:
            raise Exception('You need to pass correct refresh key')
        data={
            'client_id': self.client_data.client_id,
            'client_secret': self.client_data.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.client_data.refresh_token
        }
        strava_tokens = send_post_request(self.url, data)
        save_user_data_to_json('strava_client_data.json', strava_tokens)
        self.client_data.access_token = strava_tokens['access_token']
        self.client_data.refresh_token = strava_tokens['refresh_token']
        return self.client_data.refresh_token


"""
Use envirorment variables:  
export API_STRAVA_CLIENT_ID=000000
export API_STRAVA_CLIENT_SECRET= ZYZ
export API_STRAVA_CODE= ZYZ
"""

#new auth with code
# client_data = StravaClientData(client_id=os.getenv("API_STRAVA_CLIENT_ID"), client_secret=os.getenv('API_STRAVA_CLIENT_SECRET'),
#                                code=os.getenv('API_STRAVA_CODE'))
# auth_service=StravaAuthorification(client_data)
#auth_service.get_auth_code()
#print(auth_service.client_data.access_token)

#only renew access token with refresh token
# client_data2 = StravaClientData(client_id=os.getenv("API_STRAVA_CLIENT_ID"), client_secret=os.getenv('API_STRAVA_CLIENT_SECRET'),
#                                refresh_token=os.getenv('API_STRAVA_REFRESH_TOKEN'))
# auth_service2=StravaAuthorification(client_data2)
# refresh_token=auth_service2.refresh_access_token()
# print(auth_service2.client_data.access_token)




