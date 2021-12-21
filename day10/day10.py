def read_input(filename) -> list:
    with open(filename) as f:
        return [line for line in f.read().split()]


CHARS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_first_illegal_char(line):
    queue = []
    for char in line:
        if char in CHARS:
            queue.append(CHARS[char])
        elif char == queue[-1]:
            queue.pop()
        else:
            return char


SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}


def get_char_score(char):
    return SCORES.get(char, 0)


def part1(data):
    scores = []
    for line in data:
        first_illegal = get_first_illegal_char(line)
        score = get_char_score(first_illegal)
        scores.append(score)

    print(f"Part 1: {sum(scores)}")


def get_close_chars(line):
    queue = []
    for char in line:
        if char in CHARS:
            queue.append(CHARS[char])
        elif char == queue[-1]:
            queue.pop()
        else:
            return
    return "".join(reversed(queue))


CLOSE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def compute_score(chars):
    score = 0
    for char in chars:
        score *= 5
        score += CLOSE_SCORES[char]
    return score


def part2(data):
    scores = []
    for line in data:
        chars = get_close_chars(line)
        if not chars:
            continue
        print(line, chars)
        score = compute_score(chars)
        scores.append(score)

    middle = sorted(scores)[len(scores) // 2]

    print(f"Part 2: {middle}")


if __name__ == "__main__":
    data = read_input("day10/input.txt")
    part1(data)
    part2(data)
