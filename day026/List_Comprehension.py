# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [x*x for x in numbers]
# print(squared_numbers)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [nums for nums in numbers if nums % 2 == 0]
# print(result)
#
#
# with open("file1.txt") as f1:
#     file1 = f1.readlines()
# with open("file2.txt") as f2:
#     file2 = f2.readlines()
# result = [int(num) for num in file1 if num in file2]
# print(result)


# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanore"]
# student_score = {student: random.randint(1, 100) for student in names}
# passed_student = {student: value for (student, value) in student_score.items() if value >= 60}
# print(passed_student)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
