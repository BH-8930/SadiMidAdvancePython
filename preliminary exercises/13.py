print('رمز را وارد کنید:')
pas = str(input())
lengh = False
digit = False
upper = False

if len(pas) >= 8:
    lengh = True

for i in pas:
    if i.isupper() == True:
        upper = True
    elif i.isdigit() == True:
        digit = True

if lengh and digit and upper:
    print('Valid')
else:
    print('Invalid')