print('اعداد را وارد کنید:')
nums = input()
op = input('عملیات را وارد کنید:')
a, b = nums.split()
a, b = int(a), int(b)

def sums(a, b):
    s = a + b
    return s

def miu(a, b):
    m = a - b
    return m

def mul(a, b):
    m = a * b
    return m

def div(a, b):
    d = a / b
    return d

if op == '+':
    print(sums(a, b))
elif op == '-':
    print(miu(a, b))
elif op == '*':
    print(mul(a, b))
elif op == '/':
    print(div(a, b))
else:
    print('عملیات نامعتبر')