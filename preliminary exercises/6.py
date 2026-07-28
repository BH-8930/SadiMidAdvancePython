print('لیست را وارد نمایید.')
s = str(input())
list1 = s.split()

list1 = set(list1)

print(list(list1))