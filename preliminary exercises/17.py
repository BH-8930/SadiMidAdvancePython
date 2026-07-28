def classes(grades):

    avr = sum(grades)/len(grades)
    grades.sort()

    n = len(grades)

    if n % 2 == 1:
        median = grades[n//2]
    else:
        median = (grades[n//2-1] + grades[n//2])/ 2

    maximum = max(grades)

    return avr, median, maximum


grades = list(map(int, input().split()))

avr, median, maximum = classes(grades)

print(avr)
print(median)
print(maximum)