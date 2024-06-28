# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
