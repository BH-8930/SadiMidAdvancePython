scores = [12, 18, 9, 20, 15, 7, 19, 14] 

print("نمرات قبولی:", list(filter(lambda x: x >= 10, scores)))

print("تعداد قبول شدگان:", len(list(filter(lambda x: x >= 10, scores))))

numbers = [5, 8, 11, 14, 17, 20, 23]

print(list(filter(lambda x: x%2 == 0, numbers)))