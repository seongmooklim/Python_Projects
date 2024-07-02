# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_count, red_count, black_count ]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
