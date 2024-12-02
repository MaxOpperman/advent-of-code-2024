def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def one_a(text: list[str]) -> int:
    res = 0
    left_list = []
    right_list = []
    for line in text:
        string_locations = line.split()
        if len(string_locations) != 2 or any(not s.isdigit() for s in string_locations):
            raise ValueError(f"Invalid input: {string_locations}")
        left_list.append(string_locations[0])
        right_list.append(string_locations[1])

    left_list.sort(key=lambda x: int(x))
    right_list.sort(key=lambda x: int(x))
    for i, n in enumerate(left_list):
        left_loc = int(n)
        right_loc = int(right_list[i])
        res += abs(left_loc - right_loc)
    print(f"One A result {res}")


def one_b(text: list[str]) -> int:
    left_list = []
    right_list = []
    similarity_score = 0
    for line in text:
        string_locations = line.split()
        if len(string_locations) != 2 or any(not s.isdigit() for s in string_locations):
            raise ValueError(f"Invalid input: {string_locations}")
        left_list.append(string_locations[0])
        right_list.append(string_locations[1])

    left_list.sort(key=lambda x: int(x))
    right_list.sort(key=lambda x: int(x))
    for n in left_list:
        left_loc = int(n)
        equals = 0
        for i, m in enumerate(right_list):
            right_loc = int(m)
            if left_loc == right_loc:
                equals += 1
            elif left_loc < right_loc:
                right_list = right_list[i:]
                break
        similarity_score += equals * left_loc
    print(f"One B result {similarity_score}")


if "__main__" == __name__:
    text = read_file("./inputs/day1.txt")
    one_a(text)
    one_b(text)
