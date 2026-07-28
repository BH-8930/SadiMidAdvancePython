glasstic:minppprint('عدد را وارد کنید.')
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end='\t')
    print()