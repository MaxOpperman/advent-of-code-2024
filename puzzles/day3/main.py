import re


def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def three_a(lines: list[str]) -> int:
    command = "".join(lines)
    multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)", command)
    result = 0
    for m in multiplies:
        a, b = map(int, re.findall(r"\d{1,3}", m))
        result += a * b
    print(f"Three A result {result}")
    return result


def three_b(lines: list[str]) -> None:
    command = "".join(lines)
    split_str = re.split(r"don\'t\(\)", command)
    multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)", split_str[0])
    result = sum(
        a * b for a, b in (map(int, re.findall(r"\d{1,3}", m)) for m in multiplies)
    )
    for s in split_str[1:]:
        do_split = re.split(r"do\(\)", s)
        if len(do_split) == 1:
            continue
        elif len(do_split) >= 2:
            for do in do_split[1:]:
                multiplies = re.findall(r"mul\(\d{1,3},\d{1,3}\)", do)
                result += sum(
                    a * b
                    for a, b in (
                        map(int, re.findall(r"\d{1,3}", m)) for m in multiplies
                    )
                )
    print(f"Three B result {result}")


if "__main__" == __name__:
    text = read_file("./inputs/day3.txt")
    three_a(text)
    three_b(text)
