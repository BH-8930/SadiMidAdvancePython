def password(input):
    fname, lname, bry = input.split()
    pw = (fname.lower()[:3]) + (lname.lower()[:2]) + bry
    return pw

x = input('نام و نام خانوادگی و سال تولد را وارد کنید:')
print('رمز شما:',password(x))