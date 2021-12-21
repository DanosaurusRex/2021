def read_input(filename) -> list:
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]


def part1(inputs):
    guess = sum(inputs) // len(inputs)
    best_cost = sum([abs(x - guess) for x in inputs])

    while True:
        new_guess = guess + 1
        cost = sum([abs(x - new_guess) for x in inputs])
        if cost < best_cost:
            best_cost = cost
            guess = new_guess
            continue

        new_guess = guess - 1
        cost = sum([abs(x - new_guess) for x in inputs])
        if cost < best_cost:
            best_cost = cost
            guess = new_guess
            continue
        break

    print("Part 1:", best_cost)


def part2(inputs):
    guess = sum(inputs) // len(inputs)
    best_cost = sum([sum(range(abs(x - guess) + 1)) for x in inputs])

    while True:
        new_guess = guess + 1
        cost = sum([sum(range(abs(x - new_guess) + 1)) for x in inputs])
        if cost < best_cost:
            best_cost = cost
            guess = new_guess
            continue

        new_guess = guess - 1
        cost = sum([sum(range(abs(x - new_guess) + 1)) for x in inputs])
        if cost < best_cost:
            best_cost = cost
            guess = new_guess
            continue
        break

    print("Part 2:", best_cost)


if __name__ == "__main__":
    inputs = read_input("day7/input.txt")
    part1(inputs)
    part2(inputs)
