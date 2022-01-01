HEXBIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(hex):
    result = ""
    for char in hex:
        result += HEXBIN[char]
    return result


def decode(packet):
    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)
    values = []

    if type_id == 4:
        value = ""
        for i in range(6, len(packet), 5):
            value += packet[i + 1 : i + 5]
            if packet[i] == "0":
                value = int(value, 2)
                return version, value, packet[i + 5 :]
    else:
        length_type = int(packet[6])
        if length_type == 0:
            length = int(packet[7:22], 2)
            contents = packet[22 : 22 + length]
            while contents:
                sub_ver, sub_val, contents = decode(contents)
                version += sub_ver
                values.append(sub_val)
            packet = packet[22 + length :]
        elif length_type == 1:
            length = int(packet[7:18], 2)
            count = 0
            contents = packet[18:]
            while count < length:
                sub_ver, sub_val, contents = decode(contents)
                version += sub_ver
                values.append(sub_val)
                count += 1
            packet = contents

        match type_id:
            case 0:
                value = sum(values)
            case 1:
                value = 1
                for val in values:
                    value *= val
            case 2:
                value = min(values)
            case 3:
                value = max(values)
            case 5:
                value = int(values[0] > values[1])
            case 6:
                value = int(values[0] < values[1])
            case 7:
                value = int(values[0] == values[1])

    return version, value, packet


def part1(hex):
    packet = hex_to_bin(hex)
    version, value, rest = decode(packet)
    print(f'Part 1: {version}')


def part2(hex):
    packet = hex_to_bin(hex)
    version, value, rest = decode(packet)
    print(f'Part 2: {value}')

def read_input(filename):
    with open(filename) as f:
        return f.read().strip()


P1_TEST = [
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]

P2_TEST = [
    'C200B40A82', '04005AC33890', '880086C3E88112', 'CE00C43D881120', 'D8005AC2A8F0', 'F600BC2D8F',
    '9C005AC2F8F0', '9C0141080250320F1802104A08'
]

if __name__ == "__main__":
    hex = read_input('day16/input.txt')
    part1(hex)
    part2(hex)
