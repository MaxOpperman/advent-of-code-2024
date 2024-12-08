import itertools
import operator

from tqdm import tqdm


def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def processOps(
    formula: list[callable], data: list[int], expected: int
) -> tuple[list[callable], list[int]]:
    """
    https://stackoverflow.com/questions/44370595/how-to-iterate-through-arithmetic-operators-across-a-static-excecutable-formula
    """
    res_formula = list(formula)
    result = list(data)
    for op in formula:
        result = [op(result[0], result[1])] + result[2:]
        res_formula.remove(op)

        if len(result) == 1:
            break
        elif result[0] > expected:
            break
    return (res_formula, result)


def seven_a(results: list[int], numbers_list: list[int]) -> int:
    operators = [operator.add, operator.mul]
    res = 0
    for line_num, nums in enumerate(numbers_list):
        current_result = results[line_num]
        for f in itertools.product(operators, repeat=len(nums) - 1):
            result = list(nums)
            formula = list(f)
            formula, result = processOps(formula, result, current_result)
            # print(f"Current result: {current_result}. Temp res {result}: {formula}")
            if current_result == result[0]:
                res += current_result
                break
    print(f"Seven A result {res}")
    return res


def concatenate_operator(x: int, y: int) -> int:
    return int(str(x) + str(y))


def seven_b(results: list[int], numbers_list: list[int]) -> int:
    operators = [operator.add, operator.mul, concatenate_operator]
    res = 0
    for line_num, nums in tqdm(enumerate(numbers_list)):
        current_result = results[line_num]
        for f in itertools.product(operators, repeat=len(nums) - 1):
            result = list(nums)
            formula = list(f)
            formula, result = processOps(formula, result, current_result)
            # print(f"Current result: {current_result}. Temp res {result}: {formula}")
            if current_result == result[0]:
                res += current_result
                break
    print(f"Seven B result {res}")
    return res


if "__main__" == __name__:
    text = read_file("./inputs/day7.txt")
    results, numbers_list = [], []
    for line in text:
        line = line.split(":")
        results.append(int(line[0]))
        numbers_list.append([int(num) for num in line[1].split()])
    seven_a(results, numbers_list)
    seven_b(results, numbers_list)
