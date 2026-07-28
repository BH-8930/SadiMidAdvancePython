def parse_csv(path):

    with open(path) as csv:

        for row in csv:
            yield [x.strip() for x in row.split(",")]


def calculate_sums(file_path):

    with open("result.csv", "w") as result:

        for rows in parse_csv(file_path):
            nums = list(map(int, rows))

            sumation = sum(nums)
            nums.append(sumation)

            nums = ",".join(map(str, nums))
            
            result.write(nums + "\n")


file_path = input()
calculate_sums(file_path)