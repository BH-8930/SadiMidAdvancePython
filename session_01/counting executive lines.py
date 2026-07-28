def count_executable_lines(file_path):

    with open(file_path) as text:
        count = 0

        for line in text:
            l = line.strip()

            if l == '':
                continue

            elif l[0] == '#':
                continue

            else:
                count += 1

        return count
    
path = str(input())
print(count_executable_lines(path))