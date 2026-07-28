word = input('کلمه را وارد کنید:')

def palin(word):
    if word == word[::-1]:
        return 'Yes'
    return 'No'

print(palin(word))