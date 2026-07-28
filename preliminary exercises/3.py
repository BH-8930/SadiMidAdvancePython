count = 0

while True:
    x = input('ساعت ورود را وارد نمایید:')
    if x != 'end':
        count += 1
    if x == 'end':
        break
    
print('تعداد افراد:',count)