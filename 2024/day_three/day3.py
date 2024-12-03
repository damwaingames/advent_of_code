import re

with open("input.txt", "r") as input_file:
    instructions = input_file.read().strip()
    first_split = instructions.split(r"don't()", 1)
    part_two_instructions = first_split[0]
    next_instructions = first_split[1]
    while True:
        inactive_instructions = next_instructions.split(r"do()", 1)
        if len(inactive_instructions) == 2:
            active_instructions = inactive_instructions[1].split(r"don't()", 1)
            part_two_instructions += active_instructions[0]
        else:
            break
        next_instructions = active_instructions[1]
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, instructions)
    part_one_total = 0
    for match in matches:
        x, y = match
        part_one_total += int(x) * int(y)
    part_two_matches = re.findall(pattern, part_two_instructions)
    part_two_total = 0
    for match in part_two_matches:
        x, y = match
        part_two_total += int(x) * int(y)
    print(f"Part One: {part_one_total}")
    print(f"Part Two: {part_two_total}")
