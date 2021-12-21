def read_input(filename) -> dict:
    data = {}
    with open(filename) as f:
        for line in f.read().split():
            key, val = line.split("-")
            if key not in data:
                data[key] = []
            data[key].append(val)
            if val not in data:
                data[val] = []
            data[val].append(key)
    return data


def part1(data):

    valid_routes = []

    route = []
    current = "start"
    options = [opt for opt in data[current] if opt not in route]

    while options:
        opt = options.pop()


if __name__ == "__main__":
    data = read_input("day12/input.txt")
    print(*data.items(), sep="\n")
