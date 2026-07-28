print('نام ها را وارد نمایید:')
fname = input()
print('نام های خانوادگی را وارد نمایید:')
lname = input()
fname = fname.split()
lname = lname.split()
l = []
for i in fname:
    for j in lname:
        l.append(i + ' ' + j)

l.sort(key = len)

for x in l:
    print(x, end = '\n')