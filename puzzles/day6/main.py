from tqdm import tqdm


def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def six_a(grid=list[str]) -> int:
    object_positions = []
    guard_position = (-1, -1)
    for i, row in enumerate(grid):
        for j, col in enumerate(list(row)):
            if col == "#":
                object_positions.append((j, i))
            if col == "^":
                guard_position = (j, i)
    guard_directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current_direction = 0
    guard_covered_count = 0
    guard_covered_positions = []
    while (
        guard_position[0] < len(grid)
        and guard_position[1] < len(grid[0])
        and guard_position[0] >= 0
        and guard_position[1] >= 0
    ):
        if not guard_position in guard_covered_positions:
            guard_covered_count += 1
            guard_covered_positions.append(guard_position)
        next_position = (
            guard_position[0] + guard_directions[current_direction][0],
            guard_position[1] + guard_directions[current_direction][1],
        )
        if next_position in object_positions:
            current_direction = (current_direction + 1) % 4
        else:
            guard_position = next_position
    print(f"Six A result: {guard_covered_count}")
    return guard_covered_count


def six_b(grid=list[str]) -> int:
    object_positions = []
    guard_position = (-1, -1)
    for i, row in enumerate(grid):
        for j, col in enumerate(list(row)):
            if col == "#":
                object_positions.append((j, i))
            if col == "^":
                guard_starting_position = (j, i)
    guard_directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    new_object_locations_found = 0
    guard_covered_positions = []
    guard_position = guard_starting_position
    current_direction = 0
    while (
        guard_position[0] < len(grid)
        and guard_position[1] < len(grid[0])
        and guard_position[0] >= 0
        and guard_position[1] >= 0
    ):
        if not guard_position in guard_covered_positions:
            guard_covered_positions.append(guard_position)
        next_position = (
            guard_position[0] + guard_directions[current_direction][0],
            guard_position[1] + guard_directions[current_direction][1],
        )
        if next_position in object_positions:
            current_direction = (current_direction + 1) % 4
        else:
            guard_position = next_position
    for j, i in tqdm(guard_covered_positions):
        new_object_position = (j, i)
        guard_position = guard_starting_position
        if new_object_position == guard_position:
            continue
        current_direction = 0
        guard_covered_positions = []
        while (
            guard_position[0] < len(grid)
            and guard_position[1] < len(grid[0])
            and guard_position[0] >= 0
            and guard_position[1] >= 0
        ):
            if (
                guard_position + guard_directions[current_direction]
            ) in guard_covered_positions:
                new_object_locations_found += 1
                break
            guard_covered_positions.append(
                (guard_position + guard_directions[current_direction])
            )
            next_position = (
                guard_position[0] + guard_directions[current_direction][0],
                guard_position[1] + guard_directions[current_direction][1],
            )
            if (
                next_position in object_positions
                or next_position == new_object_position
            ):
                current_direction = (current_direction + 1) % 4
            else:
                guard_position = next_position
    print(f"Six B result: {new_object_locations_found}")
    return new_object_locations_found


if "__main__" == __name__:
    text = read_file("./inputs/day6.txt")
    six_a(text)
    six_b(text)
