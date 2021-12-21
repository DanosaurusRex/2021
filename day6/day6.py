def read_input(filename) -> list:
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]


def simulate(inputs, days):
    default = {i: 0 for i in range(9)}

    base = {i: inputs.count(i) for i in default}
    for _ in range(days):
        copy = default.copy()
        for i in sorted(base, reverse=True):
            if not i:
                copy[6] += base[0]
                copy[8] += base[0]
            else:
                copy[i - 1] = base[i]
        base = copy

    print("Count:", sum(base.values()))


if __name__ == "__main__":
    inputs = read_input("day6/input.txt")
    simulate(inputs, 80)
    simulate(inputs, 256)
