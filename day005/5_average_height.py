student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

counter = 0
sum = 0

for height in student_heights:
  counter += 1
  sum += height

print(round(sum / counter))