import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = ""
parameters = {
    'lat': 37.440559,
    'lon': 127.13583,
    'appid': api_key,
    'exclude': 'current,minutely,daily '
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
# data_slice = data['hourly'][:12]
# print(data_slice)
for i in range(7,19):
    id = data['hourly'][i]['weather'][0]['id']
    if(id<700):
        will_rain = True

if will_rain:
    print("Bring an Umbrella")

#
# https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=37.440559&lon=127.135834&appid=252dffee55c4b3c731a578a363feb106
#
# https://api.openweathermap.org/data/2.5/weather?lat=37.440559&lon=127.13583&appid=252dffee55c4b3c731a578a363feb106