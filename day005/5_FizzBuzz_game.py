nums = list()

for i in range(1, 101):
    nums.append(i)

for i in nums:
    if i % 3 == 0 and i % 15 != 0:
        print("Fizz")
        continue
    elif i % 5 == 0 and i % 15 != 0:
        print("Buzz")
        continue
    elif i % 15 == 0:
        print("FizzBuzz")
    else:
        print(nums[i-1])
