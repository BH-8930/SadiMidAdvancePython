with open("scores.txt", "w", encoding="utf-8") as file:
    for i in range(3):
        name = input("نام دانش‌آموز: ")
        score = input("نمره: ")

        file.write(name + " - " + score + "\n")