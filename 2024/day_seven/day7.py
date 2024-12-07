def do_backtrack(
    values: list[int], target: int, current_result: int, enable_concat: bool
) -> bool:
    if len(values) == 0:
        return target == current_result
    if current_result > target:
        return False
    if do_backtrack(values[1:], target, current_result + values[0], enable_concat):
        return True
    if do_backtrack(values[1:], target, current_result * values[0], enable_concat):
        return True
    if enable_concat:
        if do_backtrack(
            values[1:], target, int(str(current_result) + str(values[0])), enable_concat
        ):
            return True
    return False


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    calculations: list[list[int]] = []
    for line in lines:
        line = line.strip()
        target, operands = line.split(":", 1)
        tmp_list = [int(target)]
        tmp_list.extend(list(map(int, operands.strip().split(" "))))
        calculations.append(tmp_list)
    part_one_total = 0
    part_two_total = 0
    results: list[int] = []
    for values in calculations:
        total = values[0]
        start_value = values[1]
        remaining_values = values[2:]
        if do_backtrack(remaining_values, total, start_value, False):
            part_one_total += total
        if do_backtrack(remaining_values, total, start_value, True):
            part_two_total += total
    print(f"Part One: {part_one_total}")
    print(f"Part Two: {part_two_total}")
