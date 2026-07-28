best_name = ""
best_score = -1
total = 0
count = 0

with open("scores.txt", "r", encoding="utf-8") as file:
    for row in file:
        name, score = row.strip().split(",")
        score = int(score)

        total += score
        count += 1

        if score > best_score:
            best_score = score
            best_name = name

average = total / count

with open("result.txt", "w", encoding="utf-8") as result:
    result.writ("دانش اموز برتر" + best_name + "\n")
    result.write("نمره:" + best_score + "\n")
    result.write("معدل کلاس:" + average)

print("دانش‌آموز برتر:", best_name)
print("نمره:", best_score)
print("معدل کلاس:", average)