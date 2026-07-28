students = [" رضا ", " محمد " , " زهرا ", " علی "] 

students = iter(students)

print(next(students))
print(next(students))
print(next(students))

for i in students:
    print(i)

print(next(students))
print(next(students))
print(next(students))
print(next(students))
print(next(students))    
# وقتی اخرین عضو را نمایش میدهد و دیگر عضوی برای برگرداندن نباشد خطا میدهد
