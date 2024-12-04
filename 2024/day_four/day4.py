import re


def count_matches(input: str) -> int:
    pattern = r"XMAS"
    matches = re.findall(pattern, input)
    return len(matches)


def check_x_mas(input: list[list[str]]) -> bool:
    letters = ["M", "S"]
    if input[1][1] != "A":
        return False
    if (
        input[0][0] not in letters
        or input[2][0] not in letters
        or input[0][2] not in letters
        or input[2][2] not in letters
    ):
        return False
    if input[0][0] == input[2][2] or input[2][0] == input[0][2]:
        return False
    return True


def get_diagonals(input: list[list[str]]) -> list[list[str]]:
    height, width = len(input), len(input[0])
    return [
        [
            input[height - p + q - 1][q]
            for q in range(max(p - height + 1, 0), min(p + 1, width))
        ]
        for p in range(height + width - 1)
    ]


def get_anti_diagonals(input: list[list[str]]) -> list[list[str]]:
    height, width = len(input), len(input[0])
    return [
        [input[p - q][q] for q in range(max(p - height + 1, 0), min(p + 1, width))]
        for p in range(height + width - 1)
    ]


with open("input.txt", "r") as input_file:
    original_puzzle: list[list[str]] = []
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        original_puzzle.append(list(line))
    transposed_puzzle = [
        [original_puzzle[j][i] for j in range(len(original_puzzle))]
        for i in range(len(original_puzzle[0]))
    ]
    diagonal_puzzle = get_diagonals(original_puzzle)
    anti_diagonal_puzzle = get_anti_diagonals(original_puzzle)
    puzzles = [
        original_puzzle,
        transposed_puzzle,
        diagonal_puzzle,
        anti_diagonal_puzzle,
    ]
    part_one_matches = 0
    part_two_matches = 0
    for puzzle in puzzles:
        for row in puzzle:
            forward = "".join(row)
            row.reverse()
            backward = "".join(row)
            part_one_matches += count_matches(forward)
            part_one_matches += count_matches(backward)
    height, width = len(original_puzzle), len(original_puzzle[0])
    vertical_steps = height - 2
    horizontal_steps = width - 2
    for j in range(vertical_steps):
        for i in range(horizontal_steps):
            window = [
                [
                    original_puzzle[i][j],
                    original_puzzle[i + 1][j],
                    original_puzzle[i + 2][j],
                ],
                [
                    original_puzzle[i][j + 1],
                    original_puzzle[i + 1][j + 1],
                    original_puzzle[i + 2][j + 1],
                ],
                [
                    original_puzzle[i][j + 2],
                    original_puzzle[i + 1][j + 2],
                    original_puzzle[i + 2][j + 2],
                ],
            ]
            if check_x_mas(window):
                part_two_matches += 1
    print(f"Part One: {part_one_matches}")
    print(f"Part Two: {part_two_matches}")
