# with open("weather_data.csv") as f:
#     data = f.readlines()
# print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)


# data_list = data["temp"].to_list()
# average = round(sum(data_list) / len(data_list), 2)
# print(average)

# print(data["temp"].mean())
# max_temp = print(data["temp"].max())

# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max()])

# Convert temperatures for C to F degrees
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# temp_f = 1.8 * monday_temp + 32
# print(temp_f)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data_csv")
