print('اعداد را وارد کنید.')
num = input()
list = num.split()

if list == sorted(list):
    print('صعودی')
elif list == sorted(list, reverse=True):
    print('نزولی')
else:
    print('نامرتب')