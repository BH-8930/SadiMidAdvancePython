print('رشته را وارد نمایید.')
l = []
d = {}
count = 0

x = str(input())
l = x.split()

for i in (l):
    count = 0
    name = i
    for j in (l):
        if name == j:
            count += 1
            d[name] = count 
print(d)