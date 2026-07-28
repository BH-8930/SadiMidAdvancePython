print('سطر و ستون را وارد کنید:')
cr = input()
rows, cols = cr.split()
rows, cols = int(rows), int(cols)
k = int(input('تعداد بمب ها:'))
l = []

for i in range (k): #تبدیل کردن مختصات بمب به عدد و افزودن به لیست به صورت تاپل
    print('مختصات بمب:')
    b = input()
    x,y = b.split()
    x,y = int(x), int(y)
    l.append((x,y))
    
dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)] #لیست جهت ها

matrix = [[0 for n in range(cols)] for n in range(rows)] #ساخت ماتریس اولیه

for i in range(len(l)): # گذاشتن بمب ها در ماتریس
     a, b = l[i]
     matrix[a][b] = '*'

for i in range(rows): #حساب کردن تعداد بمب های اطراف عضو های غیر بمب
    for j in range(cols):
        
        if matrix[i][j] == '*':
           continue
       
        count = 0
        for x in dirs:
            x1, y1 = x
            x2 = x1 + j
            y2 = i -(y1)
            
            if 0 <= y2 and y2 < rows and 0 <= x2 and x2 < cols :
                if matrix[y2][x2] == '*':
                    count += 1
                    
        matrix[i][j] = count

print('ماتریس نهایی:') 

for i in range(rows):#چاپ کردن ماتریس
    for j in range(cols):

        print(matrix[i][j], end = '  ')
        if j == (cols - 1):
            print()       