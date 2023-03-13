# nums = list()
#
# for i in range(1, 101):
#     nums.append(i)
#
# for i in nums:
#     if i % 3 == 0 and i % 15 != 0:
#         print("Fizz")
#         continue
#     elif i % 5 == 0 and i % 15 != 0:
#         print("Buzz")
#         continue
#     elif i % 15 == 0:
#         print("FizzBuzz")
#     else:
#         print(nums[i-1])

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
