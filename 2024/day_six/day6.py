def execute_guard_path(
    map: dict[tuple[int, int], str],
    position: tuple[int, int],
    direction: tuple[int, int],
) -> set[tuple[int, int]]:
    positions: set[tuple[int, int]] = set()
    loop_count = 0
    max_loop = 200
    while True:
        next_position = position[0] + direction[0], position[1] + direction[1]
        if next_position not in map:
            return positions
        if loop_count > max_loop:
            return {(-1, -1)}
        if map[next_position] == "#":
            direction = -direction[1], direction[0]
        else:
            position = next_position
            if next_position in positions:
                loop_count += 1
            else:
                loop_count = 0
            positions.add(next_position)


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    map: dict[tuple[int, int], str] = {}
    for y, line in enumerate(lines):
        line = line.strip()
        for x, glyph in enumerate(line):
            map.update({(x, y): glyph})

    part_one_total = 0
    part_two_total = 0

    position = [coord for coord, glyph in map.items() if glyph == "^"][0]
    direction = (0, -1)
    all_positions = execute_guard_path(map, position, direction)
    part_one_total = len(all_positions) + 1
    for x, y in all_positions:
        map[(x, y)] = "#"
        if execute_guard_path(map, position, direction) == {(-1, -1)}:
            part_two_total += 1
        map[(x, y)] = "."
    print(f"Part One: {part_one_total}")
    print(f"Part Two: {part_two_total}")
