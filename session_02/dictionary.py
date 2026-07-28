book = { 
    "title": "Python", 
    "author": "Ahmadi", 
    "publisher": "Danesh", 
    "year": 2024, 
    "pages": 350 
}

print(book)

print(book["title"])

print(len(book.values()))

book["year"] = "2025"

book["price"] = 450000

book.pop("publisher")

print(book.keys())

print(book.values())

for key, value in book.items():
    print(f"{key} : {value}")
