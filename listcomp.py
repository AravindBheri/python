# squares = [i * i for i in range(1,11)]
# print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 10, 0]

# passed_students = [i for i in students if i >= 60]

passed_students = [i  if i >= 60 else "FAILED!!" for i in students]
print(passed_students)