def read_input(filename) -> list:
    with open(filename) as f:
        return [[int(x) for x in line] for line in f.read().split()]


def get_neighbours(data, x, y):
    height = len(data) - 1
    width = len(data[0]) - 1

    neighbours = []
    for nb_y in range(y - 1, y + 2):
        for nb_x in range(x - 1, x + 2):
            point = (nb_x, nb_y)
            if point == (x, y):
                continue
            if min(point) < 0:
                continue
            if nb_x > width or nb_y > height:
                continue
            neighbours.append(point)
    return neighbours


def part1(data):
    data = [[x for x in row] for row in data]

    total_flashes = 0

    for _ in range(100):
        flashing = set()
        flashed = set()

        for y, row in enumerate(data):
            for x, value in enumerate(row):
                new_val = value + 1
                data[y][x] = new_val
                if new_val == 10:
                    flashing.add((x, y))

        while flashing:
            x, y = flashing.pop()
            flashed.add((x, y))

            neighbours = get_neighbours(data, x, y)
            for nb_x, nb_y in neighbours:
                new_val = data[nb_y][nb_x] + 1
                data[nb_y][nb_x] = new_val
                if new_val == 10 and (nb_x, nb_y) not in (flashed | flashing):
                    flashing.add((nb_x, nb_y))

        for f_x, f_y in flashed:
            data[f_y][f_x] = 0

        total_flashes += len(flashed)

    print(f"Part 1: {total_flashes}")


def part2(data):
    data = [[x for x in row] for row in data]

    total_value = 1
    generations = 0

    while total_value:
        generations += 1

        flashing = set()
        flashed = set()

        for y, row in enumerate(data):
            for x, value in enumerate(row):
                new_val = value + 1
                data[y][x] = new_val
                if new_val == 10:
                    flashing.add((x, y))

        while flashing:
            x, y = flashing.pop()
            flashed.add((x, y))

            neighbours = get_neighbours(data, x, y)
            for nb_x, nb_y in neighbours:
                new_val = data[nb_y][nb_x] + 1
                data[nb_y][nb_x] = new_val
                if new_val == 10 and (nb_x, nb_y) not in (flashed | flashing):
                    flashing.add((nb_x, nb_y))

        for f_x, f_y in flashed:
            data[f_y][f_x] = 0

        total_value = sum([sum(row) for row in data])

    print(f"Part 2: {generations}")


if __name__ == "__main__":
    data = read_input("day11/input.txt")
    part1(data)
    part2(data)
