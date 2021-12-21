def read_input(filename, func=str) -> list:
    with open(filename) as f:
        return [func(line) for line in f.readlines()]


def part1(inputs):
    count = 0
    for prev, curr in zip(inputs, inputs[1:]):
        if curr > prev:
            count += 1

    print("Part 1:", count)


def part2(inputs):
    size = 3

    count = 0
    for i, _ in enumerate(inputs):
        prev = inputs[i : i + size]
        curr = inputs[i + 1 : i + 1 + size]
        if len(curr) < size:
            break
        if sum(curr) > sum(prev):
            count += 1

    print("Part 2:", count)


if __name__ == "__main__":
    inputs = read_input("day1/input.txt", int)
    part1(inputs)
    part2(inputs)
