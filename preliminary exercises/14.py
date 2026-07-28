print('اسامی را وارد کنید:')
s = input()
l = s.split()
k = int(input('تعداد خانه را وارد کنید:'))

for i in range(k):
    l = l[1:] + l[:1]
    
print(l)