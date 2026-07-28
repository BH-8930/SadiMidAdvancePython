def rent(dis):
    amount = 15000
    
    if 0 < dis < 4:
        return amount
    
    elif 4 <= dis < 11:
        dis -= 3
        amount += (4000 * int(dis))
        return amount
    
    elif 11 <= dis: 
        dis -= 10
        amount += (4000 * int(dis))
        return amount

d = float(input('مسافت را وارد کنید:'))
print(rent(d))
