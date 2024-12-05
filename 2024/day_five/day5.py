def get_value(rules: dict[int, set[int]], change: list[int]) -> int:
    for idx, page in enumerate(change):
        if page in rules.keys():
            rule = rules[page]
            for i in range(idx):
                if change[i] in rule:
                    return 0
    return change[len(change) // 2]


def fixed_rule_value(rules: dict[int, set[int]], change: list[int]) -> int:
    if get_value(rules, change) != 0:
        return 0
    while True:
        for idx, page in enumerate(change):
            if page in rules.keys():
                rule = rules[page]
                for i in range(idx):
                    if change[i] in rule:
                        change.append(change.pop(i))
        check_value = get_value(rules, change)
        if check_value != 0:
            return check_value


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    rules: dict[int, set[int]] = {}
    changes: list[list[int]] = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line.find("|") != -1:
            pages = line.split("|")
            node, edge = int(pages[0]), int(pages[1])
            if node in rules.keys():
                current_set = rules[node]
                current_set.add(edge)
                rules[node] = current_set
            else:
                rules.update({node: {edge}})
        else:
            temp_list = line.split(",")
            changes.append([int(x) for x in temp_list])
    part_one_total = 0
    part_two_total = 0
    for change in changes:
        part_one_total += get_value(rules, change)
        part_two_total += fixed_rule_value(rules, change)

    print(f"Part One: {part_one_total}")
    print(f"Part Two: {part_two_total}")
