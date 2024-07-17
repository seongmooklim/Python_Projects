import requests

parameters = {
    'lat' : 37.440559,
    'lon' : 127.13583,
    'appid' : '252dffee55c4b3c731a578a363feb106'
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["main"]

print(question_data)

#
# https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=37.440559&lon=127.135834&appid=252dffee55c4b3c731a578a363feb106
#
# https://api.openweathermap.org/data/2.5/weather?lat=37.440559&lon=127.13583&appid=252dffee55c4b3c731a578a363feb106