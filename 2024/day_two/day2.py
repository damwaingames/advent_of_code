from itertools import pairwise


def check_errors(lst: list[int]) -> bool:
    sorted_lst = sorted(lst)
    rev_sorted_lst = sorted(lst, reverse=True)
    abs_diffs = [abs(y - x) for x, y in pairwise(lst)]
    return (min(abs_diffs) >= 1 and max(abs_diffs) <= 3) and (
        lst == sorted_lst or lst == rev_sorted_lst
    )


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    all_reports: list[list[int]] = []
    safety = 0
    dampened = 0
    for line in lines:
        line = line.strip()
        levels = line.split(" ")
        all_reports.append([int(x) for x in levels])
    for report in all_reports:
        rslt = check_errors(report)
        if rslt:
            safety += 1
            dampened += 1
        else:
            for idx, _ in enumerate(report):
                temp = report.pop(idx)
                rslt = check_errors(report)
                if rslt:
                    dampened += 1
                    break
                else:
                    report.insert(idx, temp)
    print(f"Part one: {safety}")
    print(f"Part two: {dampened}")
