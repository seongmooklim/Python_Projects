# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
import pandas

data = pandas.read_csv("weather_data.csv")

# temp_list = data['temp'].to_list()
# mean = sum(temp_list)/len(temp_list)
# print(mean)
# print(data['temp'].max())
# print(data['condition'])
#
# max_temp = data['temp'].max()
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
f_temp = monday_temp*9/5+32
print(f"f_temp is {f_temp}")

#Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76,12,66]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_csv_file.csv")

