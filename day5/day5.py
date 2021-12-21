def read_input(filename) -> list:
    inputs = []
    with open(filename) as f:
        for line in f.readlines():
            start, end = [s for s in line.split("->")]
            start_x, start_y = [int(s) for s in start.split(",")]
            end_x, end_y = [int(s) for s in end.split(",")]
            inputs.append(((start_x, start_y), (end_x, end_y)))
    return inputs


def part1(inputs):
    # filter vertical and horizontal
    inputs = [x for x in inputs if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    
    output = {}

    for start, end in inputs:
        if start[0] == end[0]:
            i = 1
        elif start[1] == end[1]:
            i = 0

        lower, upper = sorted([start[i], end[i]])

        for j in range(lower, upper + 1):
            match i:
                case 1:
                    key = (start[0], j)
                case 0:
                    key = (j, start[1])
    
            if key not in output:
                output[key] = 0
            output[key] += 1
    
    ge_2 = [x for x in output.values() if x >= 2]

    print("Part 1:", len(ge_2))


def part2(inputs):
    output = {}

    for start, end in inputs:
        if start[0] != end[0] and start[1] != end[1]:
            x_step = 1 if start[0] < end[0] else -1
            y_step = 1 if start[1] < end[1] else -1

            for i, j in zip(range(start[0], end[0] + x_step, x_step), range(start[1], end[1] + y_step, y_step)):
                key = (i, j)
                if key not in output:
                    output[key] = 0
                output[key] += 1

        else:
            if start[0] == end[0]:
                i = 1
            elif start[1] == end[1]:
                i = 0

            lower, upper = sorted([start[i], end[i]])

            for j in range(lower, upper + 1):
                match i:
                    case 1:
                        key = (start[0], j)
                    case 0:
                        key = (j, start[1])
        
                if key not in output:
                    output[key] = 0
                output[key] += 1
    
    ge_2 = [x for x in output.values() if x >= 2]

    print("Part 2:", len(ge_2))


if __name__ == "__main__":
    inputs = read_input("day5/input.txt")
    part1(inputs)
    part2(inputs)
