# Assistant

Python app with plugins (modules), plugins=separate apps with DTO to fill in, dockerized, compatible with RPI screen's, optional use of microphone and speaker, optional eink display 

Save info to DB (cache)
  Can use redis or MongoDB

Text mode [Interface]
  Full sentences, filled with retrieved data 
  Use sms to trigger for response* (+2FA security)

Display mode [Interface]
  Web based GUI
  Could be flask template

Voice mode [Interface]
  Leon GitHub 
  Example config https://github.com/leon-ai/leon/blob/develop/skills/utilities/have_i_been_pwned/config/en.json

Bike assistant 
  Strava API https://developers.strava.com/playground/#/Athletes/getStats
  Bike stats (per week, per month, per year ) https://developers.strava.com/playground/#/Activities/getLoggedInAthleteActivities
  Bike service info (every 100 km) 
  Traseo web scrapping

IsGonnaRain?
  API: https://openweathermap.org/current#current_JSON
  How long - timeline 
  How much rain - visualized (bar)
  gif with map generator(hour after hours)*

Morning routine (Google API's)
  Calendar
  Organizer
  Weather
  News from a day*
  Gmail topics*
  SearchTheWeb
  Top results from Google, card if included 
  Organizer 
  Birthday
  Vacation organizer 
  Tasks 
  Appointments
  Costs breakdown
  Savings
