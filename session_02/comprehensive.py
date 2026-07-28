library = { 
    "books": [ 
        ("Python", "Ahmadi", 2023), 
        ("Network+", "Karimi", 2022), 
        ("Python", "Ahmadi", 2023) 
    ], 
    "subjects": {"Python", "Network", "Programming"} 
}

print(len(library["books"]))

print(library["books"][0])

print(library["books"][0][0])

library["books"].append(("Linux", "Rahimi", 2024))

library["subjects"].add("security")

print(len(library["subjects"]))

for i in library["books"]:
    for j in i:
        print(j)
    print("------------------")

print(library["subjects"])

print("Python" in library["subjects"])

library["manager"] = "Ali Ahmadi"

print(library)

