# students = ["Aravind", "Bhanu", "Amresh", "Vinay"]
# students.sort()
# students.sort(reverse = True)
# print(students)

# students = ("Aravind", "Bhanu", "Amresh", "Vinay")
# sorted_students = sorted(students)
# print(sorted_students)

students = [("Amresh", "F", 21),
            ("Aravind", "A", 21),
            ("Bhanu", "D", 22),
            ("Vinay", "B", 21),
            ("Andy", "C", 30)]

# students.sort()
# print(students)

# grade = lambda grades:grades[1]
age = lambda ages:ages[2]
sorted_students = sorted(students, key = age)
for i in sorted_students:
    print(i)