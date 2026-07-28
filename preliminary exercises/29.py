l1 = []
while True:
    x = input()
    if x == 'exit':
        exit()
    elif x == 'show':
        print(*l1)
    elif x == 'remove':
        l1.pop(0)

    else: 
        l = x.split()      
        if l[0] == "add":
            l1.append(l[1])