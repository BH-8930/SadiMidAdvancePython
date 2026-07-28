import json

student = {"نام": "علی", "سن": 16, "نمره": 19.5, "فعال": True}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False)

with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("نام:", data["نام"])
print("نمره:", data["نمره"])
print("فعال:", data["فعال"])