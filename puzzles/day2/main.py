def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def two_a(lines: list[str]) -> int:
    safe_count = 0
    for level in lines:
        numbers = level.split()
        assert all(n.isdigit() for n in numbers)
        numbers = list(map(int, numbers))
        if (
            all(n < numbers[i + 1] for i, n in enumerate(numbers[:-1]))
            and all(abs(n - numbers[i + 1]) >= 1 and abs(n - numbers[i + 1]) <= 3 for i, n in enumerate(numbers[:-1]))
        ):
            safe_count += 1
        elif (
            all(n > numbers[i + 1] for i, n in enumerate(numbers[:-1]))
            and all(abs(n - numbers[i + 1]) >= 1 and abs(n - numbers[i + 1]) <= 3 for i, n in enumerate(numbers[:-1]))
        ):
            safe_count += 1
    print(f"Two A result {safe_count}")
    return safe_count


def is_safe(numbers: list[int]) -> bool:
    if len(numbers) == 1:
        return True
    elif len(numbers) == 2 and abs(numbers[0] - numbers[1]) <= 3 and abs(numbers[0] - numbers[1]) >= 1:
        return True
    sign = 1 if numbers[0] < numbers[1] else -1
    for i, n in enumerate(numbers[:-1]):
        if sign * (numbers[i + 1] - n) > 3 or sign * (numbers[i + 1] - n) < 1:
            return False
    return True


def two_b(lines: list[str]) -> int:
    safe_count = 0
    for level in lines:
        numbers = level.split()
        assert all(n.isdigit() for n in numbers)
        numbers = list(map(int, numbers))
        if is_safe(numbers):
            safe_count += 1
        else:
            for i in range(len(numbers)):
                other_numbers = numbers[:i] + numbers[i + 1:]
                if is_safe(other_numbers):
                    safe_count += 1
                    break
    print(f"Two B result {safe_count}")
    return safe_count


if "__main__" == __name__:
    text = read_file("./inputs/day2.txt")
    two_a(text)
    two_b(text)