def divi(num):
    count = 0
    
    for i in range(1,num+1):

        if num % i == 0:
            count += 1
    return count

def aval(num):

    if num == 2 or num == 3:
        return 'Yes'
    else:
        for i in range(2,num):
                
                if num % i == 0:
                     return 'No'
                else:
                     return 'Yes'     

x = int(input())
print(aval(divi(x)))   