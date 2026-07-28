n = int(input())
avr = {}

sums = 0
count = 0
mardod = 0

for i in range(n):
    data = input().split()
    class_name = data[0]
    grades = list(map(int, data[1:]))
    
    avg = sum(grades)/len(grades)
    avr[class_name] = avg
    
    sums += sum(grades)
    count += len(grades)

    for i in grades:
        if i < 10:
            mardod += 1

best = max(avr, key=avr.get)
weakest = min(avr, key=avr.get)

print("بهترین کلاس:", best)
print("ضعیف ترین کلاس:", weakest)
print("میانگین:", sums/count)
print("مردودی ها:", mardod)