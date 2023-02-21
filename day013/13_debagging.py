############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):        #problem is in this line, because the range function return an object
    if i == 20:                 #that starts with inclusive integer and stops exclusive integer
      print("You got it")       #we should to replace 20 to 21 and code will be work
my_function()

# Reproduce the Bug
from random import randint                      #the bug isn`t reproduce when randint function choice is 6
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]   #indexes of list should be in range from 0 to 5
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:                     #bug reproduce when entering 1994 year
  print("You are a millenial.")                     #to fix this should be >= 1994
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors
age = input("How old are you?")         #should use int() function, because input() function only read a string
if age > 18:
print(f"You can drive at age {age}.")    #missed 4 blankes for indented block after 'if' statement

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words == pages * word_per_page                        #should use assignment statement, not the comparison
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)                   #missed 4 blankes in 41 line for indented block after 'if' statement
  print(b_list)                             #so append() function use only last item from the list

mutate([1,2,3,5,8,13])