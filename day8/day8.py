def read_input(filename) -> list:
    inputs = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.split("|")
            inputs.append((line[0].split(), line[1].split()))
    return inputs


def part1(inputs):
    count = 0

    for sigs, outs in inputs:
        for num in outs:
            if len(num) in (2, 3, 4, 7):
                count += 1

    print("Part 1:", count)


def part2(inputs):
    total = 0

    for sigs, outs in inputs:
        encode = {}
        encode[1] = [sig for sig in sigs if len(sig) == 2][0]
        encode[4] = [sig for sig in sigs if len(sig) == 4][0]
        encode[7] = [sig for sig in sigs if len(sig) == 3][0]
        encode[8] = [sig for sig in sigs if len(sig) == 7][0]

        sixes = [sig for sig in sigs if len(sig) == 6]
        encode[9] = [sig for sig in sixes if not set(encode[4]) - set(sig)][0]
        sixes.remove(encode[9])
        encode[0] = [sig for sig in sixes if not set(encode[1]) - set(sig)][0]
        sixes.remove(encode[0])
        encode[6] = sixes[0]

        fives = [sig for sig in sigs if len(sig) == 5]
        encode[3] = [sig for sig in fives if not set(encode[1]) - set(sig)][0]
        fives.remove(encode[3])
        encode[5] = [sig for sig in fives if not set(sig) - set(encode[6])][0]
        fives.remove(encode[5])
        encode[2] = fives[0]

        decode = {"".join(sorted(v)): str(k) for k, v in encode.items()}
        output = ""
        for out in outs:
            key = "".join(sorted(out))
            output += decode[key]
        total += int(output)

    print("Part 2:", total)


if __name__ == "__main__":
    inputs = read_input("day8/input.txt")
    part1(inputs)
    part2(inputs)
