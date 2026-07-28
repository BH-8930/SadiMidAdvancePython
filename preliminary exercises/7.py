print('رشته را وارد نمایید.')
s = str(input())
ch = ''

while s != '':
    if s[-1] != '=':
        ch += s[-1]
        s = s[:-1]
    elif s[-1] == '=':
        s = s[:-2]

print(ch[::-1])