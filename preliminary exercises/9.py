print('ساعت را وارد کنید. در صورت رند بودن ساعت برای دقیقه ۰ وارد کنید.')
hour = input()
print('دقیقه های اینده را وارد نمایید.')
k = int(input())

s = hour.split()
hh = int(s[0])
mm = int(s[1])

if k < 60:
    if k + mm == 60:
        mm = 0
        hh += 1
    else:
        mm += k
elif k >= 60:
    hh += k//60
    mm += k%60
if hh == 24:
    hh = 0

print('ساعت محاسبه شده:',mm,hh)

