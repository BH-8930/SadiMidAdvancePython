x = int(input('عدد را وارد کنید:'))

def aval(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
            
print(aval(x))