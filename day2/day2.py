def read_input(filename) -> list:
    inputs = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.split()
            inputs.append((line[0], int(line[1])))
    return inputs


def part1(inputs):
    x = 0
    y = 0
    for command, amt in inputs:
        match command:
            case 'forward':
                x += amt
            case 'up':
                y -= amt
            case 'down':
                y += amt
    
    print("Part 1:", x * y)


def part2(inputs):
    x = 0
    y = 0
    aim = 0

    for command, amt in inputs:
        match command:
            case 'forward':
                x += amt
                y += aim * amt
            case 'up':
                aim -= amt
            case 'down':
                aim += amt

    print("Part 2:", x * y)


if __name__ == "__main__":
    inputs = read_input("day2/input.txt")
    part1(inputs)
    part2(inputs)
