import copy


def read_file(input_file: str) -> list[list[str]]:
    with open(input_file, "r") as f:
        return [list(line.strip()) for line in f]


def out_of_bounds(node: tuple[int], lines: list[list[str]]) -> bool:
    x, y = node
    return x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines)


def eight_a(lines: list[list[str]]) -> int:
    res = 0
    new_map = copy.deepcopy(lines)
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char != ".":
                start_i = i + 1
                for j2, line2 in enumerate(lines[j:], start=j):
                    for i2, char2 in enumerate(line2[start_i:], start=start_i):
                        if char2 == char:
                            # draw a line through the coordinates and the line has length 3* the distance
                            # add the end points of the line as the antinodes
                            y_diff = j2 - j
                            if i >= i2:
                                x_diff = i - i2
                                antinode1 = (i + x_diff, j - y_diff)
                                antinode2 = (i2 - x_diff, j2 + y_diff)
                            else:
                                x_diff = i2 - i
                                antinode1 = (i - x_diff, j - y_diff)
                                antinode2 = (i2 + x_diff, j2 + y_diff)
                            if not out_of_bounds(antinode1, lines):
                                new_map[antinode1[1]][antinode1[0]] = "#"
                            if not out_of_bounds(antinode2, lines):
                                new_map[antinode2[1]][antinode2[0]] = "#"
                    start_i = 0
    # count the hashtags
    for line in new_map:
        res += line.count("#")
    print(f"Eight A result {res}")
    return res


def eight_b(lines: list[list[str]]) -> int:
    res = 0
    new_map = copy.deepcopy(lines)
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char != ".":
                start_i = i + 1
                for j2, line2 in enumerate(lines[j:], start=j):
                    for i2, char2 in enumerate(line2[start_i:], start=start_i):
                        if char2 == char:
                            # draw a line through the coordinates and the line has length 3* the distance
                            # add the end points of the line as the antinodes
                            y_diff = j2 - j
                            if i >= i2:
                                x_diff = i - i2
                                antinode1 = (i + x_diff, j - y_diff)
                                while not out_of_bounds(antinode1, lines):
                                    new_map[antinode1[1]][antinode1[0]] = "#"
                                    antinode1 = (
                                        antinode1[0] + x_diff,
                                        antinode1[1] - y_diff,
                                    )

                                antinode2 = (i2 - x_diff, j2 + y_diff)
                                while not out_of_bounds(antinode2, lines):
                                    new_map[antinode2[1]][antinode2[0]] = "#"
                                    antinode2 = (
                                        antinode2[0] - x_diff,
                                        antinode2[1] + y_diff,
                                    )
                            else:
                                x_diff = i2 - i
                                antinode1 = (i - x_diff, j - y_diff)
                                while not out_of_bounds(antinode1, lines):
                                    new_map[antinode1[1]][antinode1[0]] = "#"
                                    antinode1 = (
                                        antinode1[0] - x_diff,
                                        antinode1[1] - y_diff,
                                    )
                                antinode2 = (i2 + x_diff, j2 + y_diff)
                                while not out_of_bounds(antinode2, lines):
                                    new_map[antinode2[1]][antinode2[0]] = "#"
                                    antinode2 = (
                                        antinode2[0] + x_diff,
                                        antinode2[1] + y_diff,
                                    )
                    start_i = 0
    # count the elements that are not "."
    for line in new_map:
        res += sum(1 for char in line if char != ".")
    print(f"Eight B result {res}")
    return res


if "__main__" == __name__:
    text = read_file("./inputs/day8.txt")
    eight_a(text)
    eight_b(text)
