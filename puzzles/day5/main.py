from tqdm import tqdm


def read_file(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        return [line.strip() for line in f]


def five_a(page_order = list[tuple[int, int]], updates = list[str]) -> tuple[int, list[int]]:
    correct_updates, incorrect_updates = [], []
    for u in updates:
        update_pages = [int(num) for num in u.split(",")]
        seen = []
        correct_order = True
        for update_page in update_pages:
            for page in page_order:
                if page[0] == update_page and page[1] in seen:
                    correct_order = False
                    break
            seen.append(update_page)
        if correct_order:
            correct_updates.append(update_pages)
        else:
            incorrect_updates.append(update_pages)
    res = 0
    for u in correct_updates:
        res += int(u[int((len(u) - 1)/2)])
    print(f"Five A result: {res}")
    return res, incorrect_updates


def check_order(page_order = list[tuple[int, int]], updates = list[int]) -> tuple[bool, int]:
    seen = []
    for i, update_page in enumerate(updates):
        for page in page_order:
            if page[0] == update_page and page[1] in seen:
                return False, i
            seen.append(update_page)
    return True, -1


def five_b(page_order = list[tuple[int, int]], updates = list[str]) -> int:
    new_correct_updates = []
    for u in tqdm(updates):
        update_pages = [int(num) for num in u.split(",")]
        correct_order, ind = check_order(page_order, update_pages)
        if correct_order == True:
            # we only handle incorrect updates
            continue
        # we need to find the correct page order
        swap_i = 1
        current_page_rules = []
        for page in page_order:
            if page[0] in update_pages or page[1] in update_pages:
                current_page_rules.append(page)
        while not correct_order:
            update_pages[abs(ind - swap_i)], update_pages[ind] = update_pages[ind], update_pages[abs(ind - swap_i)]
            partial_correct_order, ind = check_order(current_page_rules, update_pages[:ind])
            if not partial_correct_order:
                swap_i += 1
                continue
            else:
                correct_order, ind = check_order(current_page_rules, update_pages)
                swap_i = 1
        new_correct_updates.append(update_pages)
    res = 0
    for u in new_correct_updates:
        res += int(u[int((len(u) - 1)/2)])
    print(f"Five B result: {res}")
    return res
            


if "__main__" == __name__:
    text = read_file("./inputs/day5.txt")
    page_order, updates = text[:text.index("")], text[text.index("") + 1:]
    page_order = [tuple([int(page) for page in line.split("|")]) for line in page_order]
    five_a(page_order, updates)
    five_b(page_order, updates)

