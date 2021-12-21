def read_input(filename) -> list:
    with open(filename) as f:
        return [[int(c) for c in line] for line in f.read().split()]


def get_low_points(grid):
    low_points = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            adj_points = get_adj_points(grid, x, y)
            adj_values = [grid[y][x] for x, y in adj_points]
            if val < min(adj_values):
                low_points.append((x, y))
    return low_points


def get_adj_points(grid, x, y):
    width = len(grid[0]) - 1
    height = len(grid) - 1

    adj_points = []
    if y != 0:
        adj_points.append((x, y - 1))
    if x != 0:
        adj_points.append((x - 1, y))
    if y != height:
        adj_points.append((x, y + 1))
    if x != width:
        adj_points.append((x + 1, y))
    return adj_points


def get_risk_score(grid, low_points):
    return sum([grid[y][x] + 1 for x, y in low_points])


def part1(inputs):
    low_points = get_low_points(inputs)
    risk_score = get_risk_score(inputs, low_points)
    print(f"Part 1: {risk_score}")


def part2(grid):
    basins = []
    visited = set()

    for root_y, row in enumerate(grid):
        for root_x, val in enumerate(row):
            if val == 9:
                continue
            if (root_x, root_y) in visited:
                continue

            basin_points = set()

            to_visit = set([(root_x, root_y)])
            while to_visit:
                x, y = to_visit.pop()

                adj_points = get_adj_points(grid, x, y)
                basin_adj_points = [
                    (x_i, y_i) for x_i, y_i in adj_points if grid[y_i][x_i] < 9
                ]
                for point in basin_adj_points:
                    if point not in visited:
                        to_visit.add(point)

                visited.add((x, y))
                basin_points.add((x, y))

            basins.append(basin_points)

    basin_sizes = [len(basin) for basin in basins]
    a, b, c = sorted(basin_sizes)[-3:]
    print(f"Part 2: {a*b*c}")


if __name__ == "__main__":
    grid = read_input("day9/input.txt")
    part1(grid)
    part2(grid)
