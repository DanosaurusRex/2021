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
    paths = [['start']]

    while True:
        new_paths = []
        for path in paths.copy():
            last = path[-1]
            if last == 'end':
                new_paths.append(path)
                continue
            for option in data[last]:
                if option in path and option.islower():
                    continue
                new_path = path + [option]
                new_paths.append(new_path)
        if paths == new_paths:
            break
        paths = new_paths

    print(f'Part 1: {len(paths)}')


def part2(data):
    doubles = [key for key in data if key.islower() and key not in ('start', 'end')]

    print(doubles)
    paths = []

    for double in doubles:
        print(double)
        double_paths = [['start']]
        while True:
            new_paths = []
            for path in double_paths.copy():
                last = path[-1]
                if last == 'end':
                    new_paths.append(path)
                    continue
                for option in data[last]:
                    if option.islower():
                        if path.count(option) == 2:
                            continue
                        if option in path and option != double:
                            continue
                    new_path = path + [option]
                    new_paths.append(new_path)
            if double_paths == new_paths:
                break
            double_paths = new_paths

        for path in double_paths:
            if path not in paths:
                paths.append(path)


    print(*paths, sep='\n')

    print(f'Part 2: {len(paths)}')


if __name__ == "__main__":
    data = read_input("day12/input.txt")
    part1(data)
    part2(data)
