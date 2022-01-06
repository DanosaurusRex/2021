import re

pair_re = re.compile(r"\[(\d+),(\d+)\]")


def sf_add(left, right):
    return f"[{left},{right}]"


def sf_explode(text):
    i = 0
    while True:
        m = pair_re.search(text, i)
        if not m:
            return

        before = before = text[: m.start()]
        if before.count("[") > (before.count("]") + 3):
            break

        i = m.end()

    after = text[m.end() :]
    res = ""

    left = re.search(r"\d+", before[::-1])
    if left:
        start = len(before) - left.end()
        end = len(before) - left.start()
        num = before[start:end]
        res += before[:start]
        res += str(int(num) + int(m.group(1)))
        res += before[end:]
    else:
        res += before

    res += "0"

    right = re.search(r"\d+", after)
    if right:
        res += after[: right.start()]
        res += str(int(right.group(0)) + int(m.group(2)))
        res += after[right.end() :]
    else:
        res += after
    return res


def sf_split(text):
    m = re.search(r"\d{2}", text)
    if not m:
        return

    whole = int(m.group(0))
    half = whole // 2
    res = ""
    res += text[: m.start()]
    res += f"[{half},{half + (whole % 2)}]"
    res += text[m.end() :]
    return res


def sf_reduce(text):
    while True:
        exploded = sf_explode(text)
        if exploded:
            text = exploded
            continue
        splitted = sf_split(text)
        if splitted:
            text = splitted
            continue
        return text


def sf_magnitude(text):
    while True:
        m = pair_re.search(text)
        if not m:
            return int(text)
        value = (int(m.group(1)) * 3) + (int(m.group(2)) * 2)
        text = text[: m.start()] + str(value) + text[m.end() :]


def read_input(filename):
    with open(filename) as f:
        return f.read().split()


def part1(sf_nums):
    sf_num = sf_nums[0]

    for second in sf_nums[1:]:
        sf_num = sf_add(sf_num, second)
        sf_num = sf_reduce(sf_num)

    mag = sf_magnitude(sf_num)

    print(f"Part 1: {mag}")


def part2(sf_nums):
    best = 0

    for left in sf_nums:
        for right in sf_nums:
            if left == right:
                continue
            sf_num = sf_add(left, right)
            sf_num = sf_reduce(sf_num)
            mag = sf_magnitude(sf_num)
            if mag > best:
                best = mag

    print(f"Part 2: {best}")


if __name__ == "__main__":
    sf_nums = read_input("day18/input.txt")
    part1(sf_nums)
    part2(sf_nums)
