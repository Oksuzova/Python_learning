numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [x*x for x in numbers]
print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [nums for nums in numbers if nums % 2 == 0]
print(result)
