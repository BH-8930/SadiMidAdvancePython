n = int(input())
times = []

for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort()
conflict = False

for i in range(n-1):
    if times[i][1] > times[i+1][0]:
        conflict = True
        break

if conflict:
    print("Conflict")
else:
    print("No Conflict")