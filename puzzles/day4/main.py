def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def r_search(
    grid: list[list[str]], word: str, index: int, x: int, y: int, dir: str
) -> bool:
    """
    https://github.com/maximiliantiao/word_search_solver
    """
    # Word found
    if index == len(word):
        return True
    # Searching beyond grid boundary
    elif (x < 0) or (y < 0) or (x == len(grid[0])) or (y == len(grid)):
        return False
    # Continue searching in current direction
    else:
        # If current character is found
        if grid[y][x] == word[index]:
            index += 1
            # Search N direction
            if dir == "N" and r_search(grid, word, index, x, y - 1, "N"):
                return True
            # Search NE direction
            elif dir == "NE" and r_search(grid, word, index, x + 1, y - 1, "NE"):
                return True
            # Search E direction
            elif dir == "E" and r_search(grid, word, index, x + 1, y, "E"):
                return True
            # Search SE direction
            elif dir == "SE" and r_search(grid, word, index, x + 1, y + 1, "SE"):
                return True
            # Search S direction
            elif dir == "S" and r_search(grid, word, index, x, y + 1, "S"):
                return True
            # Search SW direction
            elif dir == "SW" and r_search(grid, word, index, x - 1, y + 1, "SW"):
                return True
            # Search W direction
            elif dir == "W" and r_search(grid, word, index, x - 1, y, "W"):
                return True
            # Search NW direction
            elif dir == "NW" and r_search(grid, word, index, x - 1, y - 1, "NW"):
                return True
            else:
                return False
        # If current character is not found
        else:
            return False


def base_search(grid: list[list[str]], word: str) -> int:
    """
    https://github.com/maximiliantiao/word_search_solver
    """
    count = 0
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    # Iterate through each row of word search grid
    for y in range(len(grid)):
        # Iterate through each column of word search grid
        for x in range(len(grid[y])):
            # Locate first letter of words
            if grid[y][x] == word[0]:
                for direction in directions:
                    if r_search(grid, word, 0, x, y, direction):
                        count += 1
    return count


def x_search(grid: list[list[str]], word: str) -> int:
    found_at = []
    # Iterate through each row of word search grid
    for y in range(len(grid)):
        # Iterate through each column of word search grid
        for x in range(len(grid[y])):
            # Locate first letter of words
            if grid[y][x] == word[0]:
                if r_search(grid, word, 0, x, y, "NE"):
                    found_at.append((x, y, "NE"))
                if r_search(grid, word, 0, x, y, "SE"):
                    found_at.append((x, y, "SE"))
                if r_search(grid, word, 0, x, y, "SW"):
                    found_at.append((x, y, "SW"))
                if r_search(grid, word, 0, x, y, "NW"):
                    found_at.append((x, y, "NW"))
    # only return the number of times MAS appears in an X
    a_coordinates = []
    for curr in found_at:
        # get the current x and y
        x, y, direction = curr
        if direction == "NE":
            if (x, y - 2, "SE") in found_at:
                a_coordinates.append((x + 1, y - 1))
            elif (x + 2, y, "NW") in found_at:
                a_coordinates.append((x + 1, y - 1))
        elif direction == "SE":
            if (x, y + 2, "NE") in found_at:
                a_coordinates.append((x + 1, y + 1))
            elif (x + 2, y, "SW") in found_at:
                a_coordinates.append((x + 1, y + 1))
        elif direction == "NW":
            if (x, y - 2, "SW") in found_at:
                a_coordinates.append((x - 1, y - 1))
            elif (x - 2, y, "NE") in found_at:
                a_coordinates.append((x - 1, y - 1))
        elif direction == "SW":
            if (x, y + 2, "NW") in found_at:
                a_coordinates.append((x - 1, y + 1))
            elif (x - 2, y, "SE") in found_at:
                a_coordinates.append((x - 1, y + 1))
    return len(set(a_coordinates))


def four_a(lines: list[str]) -> int:
    word = "XMAS"
    puzzle_grid = [list(line) for line in lines]
    res = base_search(puzzle_grid, word)
    print(f"Four A result {res}")


def four_b(lines: list[str]) -> int:
    word = "MAS"
    puzzle_grid = [list(line) for line in lines]
    res = x_search(puzzle_grid, word)
    print(f"Four B result {res}")


if "__main__" == __name__:
    text = read_file("./inputs/day4.txt")
    four_a(text)
    four_b(text)
