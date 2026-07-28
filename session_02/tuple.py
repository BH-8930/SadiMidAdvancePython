student = ("رضا", "علی", "محمد", "زهرا", "علی")

print(student)

print(len(student))

print(student[2])

print("محمد" in student)

print(student.count("محمد"))

print(student.index("رضا"))

print(student[:2])

for i in student:
    print(i)

student = list(student)
student.append("سارا")
student = tuple(student)
print(student)

x = input()
if x in student:
    print(student.index(x))
else:
    print("نام وجود ندارد")