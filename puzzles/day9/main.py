from collections import OrderedDict
import operator

from tqdm import tqdm


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
    # print("".join(disk))
    # find the index of the last . in the disk
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
    # print("".join(disk))
    res = 0
    for i, char in enumerate(disk):
        if char == ".":
            break
        else:
            res += i * int(char)
    print(f"Nine A result {res}")
    return res

# def nine_b(line: str) -> int:
#     # free space holds [ID]: number of spaces it uses.
#     free_space = OrderedDict()
#     used_space = OrderedDict()
#     for i, block_len in enumerate(line):
#         if i % 2 == 0:
#             used_space[i // 2] = int(block_len)
#         else:
#             free_space[i // 2] = int(block_len)
#             used_space[i] = 0
#     while len(free_space) > 0:
#         for key, value in tqdm(reversed(free_space.items())):


if "__main__" == __name__:
    text = read_file("./inputs/day9.txt")
    assert len(text) == 1
    nine_a(text[0])
    # nine_b(text[0])
