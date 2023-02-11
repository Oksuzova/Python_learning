student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

tmp = 0

for i in student_scores:
    if tmp < i:
        tmp = i

print("The highest score in the class is:", tmp)
