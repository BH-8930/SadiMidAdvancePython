d = {'present': 0, 'absent': 0}

print('لیست را وارد کنید:')
x = input()
l = x.split()

for i in l:
    if i == 'present':
        d['present'] += 1
    elif i == 'absent':
        d['absent'] += 1
        
print(d)