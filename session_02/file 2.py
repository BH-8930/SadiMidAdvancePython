with open("text.txt", "w") as file:
    file.write("Python Programming")

with open("text.txt", "r") as file:
    text = file.read()

count = 0

for ch in text:
    if ch.isalpha():
        count += 1

print("تعداد حروف انگلیسی:", count)