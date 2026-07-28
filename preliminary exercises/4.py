l = []

while True:
    x = input('شماره را وارد کنید:')
    if x == '0':
       break
    elif x != '0':
       l.append(x)

print(*list(reversed(l)))       

