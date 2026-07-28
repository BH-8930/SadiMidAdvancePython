with open("notes.txt", "w", encoding="utf-8") as file:
    
    file.write("نام مدرسه: استعدادهای درخشان سعدی\n")
    file.write("نام درس: پایتون\n")
    file.write("سال: ۱۴۰۵\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())