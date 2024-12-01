with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    first_list, second_list = [], []
    for line in lines:
        a, b = line.split()
        first_list.append(a)
        second_list.append(b)
    first_list.sort()
    second_list.sort()
    diff_list: list[int] = []
    for i, x in enumerate(first_list):
        diff_list.append(abs(int(x) - int(second_list[i])))
    print(f"Part One: {sum(diff_list)}")
    similarity_list: list[int] = []
    for x in first_list:
        similarity_list.append(int(x) * second_list.count(x))
    print(f"Part Two: {sum(similarity_list)}")
