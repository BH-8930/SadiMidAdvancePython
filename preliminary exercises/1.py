t = float(input('Enter the temperature:'))

if t <= 0:
    print('Ice')
elif 99>= t >= 1:
    print('Water')
elif t <= 100:
    print('Steam')
