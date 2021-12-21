def read_input(filename) -> list:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def part1(inputs):
    gamma = ""
    epsilon = ""

    for i, _ in enumerate(inputs[0]):
        bit_list = [rec[i] for rec in inputs]
        if bit_list.count("1") > bit_list.count("0"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)

    print("Part 1:", gamma_int * epsilon_int)


def part2(inputs):
    ox = ""
    co = ""

    for i, _ in enumerate(inputs[0]):
        ox_list = [rec for rec in inputs if rec.startswith(ox)]

        if len(ox_list) == 1:
            ox = ox_list[0]
        else:
            ox_bit_list = [rec[i] for rec in ox_list]
            if ox_bit_list.count("1") >= ox_bit_list.count("0"):
                ox += "1"
            else:
                ox += "0"

        co_list = [rec for rec in inputs if rec.startswith(co)]

        if len(co_list) == 1:
            co = co_list[0]
        else:
            co_bit_list = [rec[i] for rec in co_list]
            if co_bit_list.count("1") >= co_bit_list.count("0"):
                co += "0"
            else:
                co += "1"

    ox_int = int(ox, 2)
    co_int = int(co, 2)

    print("Part 2:", ox_int * co_int)


if __name__ == "__main__":
    inputs = read_input("day3/input.txt")
    part1(inputs)
    part2(inputs)
