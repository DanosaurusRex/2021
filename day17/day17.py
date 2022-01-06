def read_input(filename):
    with open(filename) as f:
        data = f.read().strip()
        x = [int(v) for v in data[data.index("x") + 2 : data.index(",")].split("..")]
        y = [int(v) for v in data[data.index("y") + 2 :].split("..")]
        return x, y


def simulate(x, y, target):
    pos = (0, 0)
    vel = (x, y)

    while True:
        pos = update_pos(pos, vel)
        if hit_target(pos, target):
            return True
        if missed_target(pos, target):
            return False
        vel = update_vel(vel)


def hit_target(pos, target):
    x, y = pos
    tar_x, tar_y = target
    in_x = x >= min(tar_x) and x <= max(tar_x)
    in_y = y >= min(tar_y) and y <= max(tar_y)
    return in_x and in_y


def missed_target(pos, target):
    x, y = pos
    tar_x, tar_y = target
    missed_x = x > max(tar_x)
    missed_y = y < min(tar_y)
    return missed_x or missed_y


def update_vel(vel):
    x, y = vel
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1
    y -= 1
    return x, y


def update_pos(pos, vel):
    x, y = pos
    vel_x, vel_y = vel
    x += vel_x
    y += vel_y
    return x, y


def part1(target):
    min_y = min(target[1])
    ans = max_distance(min_y)
    print(f"Part 1: {ans}")


def max_distance(n):
    return n * (n + 1) // 2


def part2(target):
    valid = []
    tar_x = target[0]
    tar_y = target[1]

    max_y = -tar_y[0] - 1

    for x in range(tar_x[1] + 1):
        furthest = max_distance(x)
        if furthest < tar_x[0]:
            continue

        for y in range(tar_y[0], max_y + 1):
            if simulate(x, y, target):
                valid.append((x, y))

    print(f"Part 2: {len(valid)}")


if __name__ == "__main__":
    data = read_input("day17/input.txt")
    part1(data)
    part2(data)
