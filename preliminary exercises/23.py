numbers = list(map(int, input().split()))

csum = numbers[0]
msum = numbers[0]

for i in numbers[1:]:
    if csum < 0:
        csum = i
    else:
        csum += i

    if csum > msum:
        msum = csum

print(msum)