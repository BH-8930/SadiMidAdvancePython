with open("student.txt", 'w', encoding= 'UTF-8') as f:

    f.write("علی\n")
    f.write("زهرا\n")
    f.write("فاطمه\n")

with open("student.txt", 'r', encoding= 'UTF-8') as f:

    print(f.read())

new = input()

with open("student.txt", 'a', encoding= 'UTF-8') as f:
    f.write(new + "\n")

with open("student.txt", 'r', encoding= 'UTF-8') as f:
    print(f.read())

    count = 1
with open("student.txt", 'r', encoding= 'UTF-8') as f:

    count = 1

    for line in f:
        print(f"{count}- {line}")
        count += 1