dict = {}
total = 0
while True:
    print('commands: add - remove - total - exit')
    x = input()
    if x == 'total':
        print(dict)
        print('total=', total)
    elif x == 'exit':
        exit()
    else:
        order = x.split()
        if order[0] == 'add':
            if order[1] in dict:
                dict[order[1]] += int(order[2])
                total += int(order[2])
            else:
                dict[order[1]] = int(order[2])
                total += int(order[2])
        if order[0] == 'remove':
            if order[1] not in dict:
                print('این محسول در لیست کالاها وجود ندارد')
            else:
                total -= dict[order[1]]
                dict.pop(order[1])
                