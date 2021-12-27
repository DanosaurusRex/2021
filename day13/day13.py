def read_input(filename):
    points = set()
    instructions = []
    with open(filename) as f:
        for line in f.read().split():
            if ',' in line:
                x, y = line.split(',')
                point = int(x), int(y)
                points.add(point)
            elif '=' in line:
                axis, fold = line.split('=')
                axis = axis[-1]
                instructions.append((axis, int(fold)))
    return points, instructions


def get_index(axis):
    if axis == 'x':
        return 0
    else:
        return 1

def do_fold(points, fold, index):
    new_points = set()
    for point in points:
        point = list(point)
        if point[index] > fold:
            point[index] = fold - abs(point[index] - fold)
        new_points.add(tuple(point))
    return new_points

def part1(points, instructions):
    axis, fold = instructions[0]

    index = get_index(axis)
    points = do_fold(points, fold, index)
    
    print(f'Part 1: {len(points)}')


def draw(points, printlog=True):
    x = max([x for x, y in points]) + 1
    y = max([y for x, y in points]) + 1

    output = [[' '] * x for _ in range(y)]

    for x, y in points:
        output[y][x] = '#'
    
    if printlog:
        for line in output:
            print(''.join(line))
    return output

def part2(points, instructions):
    for axis, fold in instructions:
        index = get_index(axis)
        points = do_fold(points, fold, index)

    draw(points)



if __name__ == '__main__':
    points, instructions = read_input('day13/input.txt')
    part1(points, instructions)
    part2(points, instructions)
