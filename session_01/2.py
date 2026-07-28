with open("books.txt", "r", encoding="utf-8") as file:
    books = file.readlines()

count = len(books)

print("تعداد کتاب‌ها:", count)