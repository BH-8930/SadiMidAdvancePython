print('اعداد را وارد کنید:')
x = input()
l = x.split()
l1 = []
max1 = float('-inf')
max2 = float('-inf')
   
for i in l:
    num = int(i)

    if num > max1:
        max2 = max1
        max1 = num

    elif max1 > num > max2:
        max2 = num

print('دومین عدد بزرگ:',max2)        