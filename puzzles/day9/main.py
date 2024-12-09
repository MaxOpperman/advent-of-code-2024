import operator


def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def nine_a(line: str) -> int:
    disk = []
    for i, block_len in enumerate(line):
        if i % 2 == 0:
            disk.extend([str(i // 2) for _ in range(int(block_len))])
        else:
            disk.extend(["." for _ in range(int(block_len))])
    last_dot = len(disk) - operator.indexOf(reversed(disk), ".") - 1
    current_right_index = len(disk) - 1
    for i, char in enumerate(disk[:last_dot]):
        if char == ".":
            disk[i] = disk[current_right_index]
            disk[current_right_index] = "."
            while disk[current_right_index] == ".":
                current_right_index -= 1
        if current_right_index <= i:
            break
    res = 0
    for i, char in enumerate(disk):
        if char == ".":
            break
        else:
            res += i * int(char)
    print(f"Nine A result {res}")
    return res


class Space:
    def __init__(self, id: int | None, used: bool, size: int):
        self.id = id
        self.used = used
        self.size = size

    def __repr__(self):
        return f"Space {self.id} of size {self.size} is used: {self.used}"


def nine_b(line: str) -> int:
    disk = []
    for i, block_len in enumerate(line):
        if i % 2 == 0:
            disk.append(Space(i // 2, True, int(block_len)))
        else:
            disk.append(Space(None, False, int(block_len)))
    i = 0
    while i < len(disk):
        free_space = disk[i]
        next_i = True
        if not free_space.used:
            for j, used_space in enumerate(disk[::-1]):
                if len(disk) - j - 1 < i:
                    break
                if used_space.used:
                    if used_space.size == free_space.size:
                        disk[i] = Space(used_space.id, True, used_space.size)
                        disk[-j - 1] = Space(None, False, used_space.size)
                        break
                    elif used_space.size < free_space.size:
                        next_i = False
                        disk[i] = Space(used_space.id, True, used_space.size)
                        disk[-j - 1] = Space(None, False, used_space.size)
                        disk.insert(
                            i + 1, Space(None, False, free_space.size - used_space.size)
                        )
                        break
        if next_i:
            i += 1
    res = 0
    counter = 0
    for space in disk:
        if space.used:
            for i in range(space.size):
                res += counter * space.id
                counter += 1
        else:
            counter += space.size
    print(f"Nine B result {res}")
    return res


if "__main__" == __name__:
    text = read_file("./inputs/day9.txt")
    assert len(text) == 1
    nine_a(text[0])
    nine_b(text[0])
