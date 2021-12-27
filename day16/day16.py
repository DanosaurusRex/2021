HEXBIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def hex_to_bin(hex):
    result = ''
    for char in hex:
        result += HEXBIN[char]
    return result

def get_version(packet):
    return int(packet[:3], 2)

def get_type(packet):
    return int(packet[3:6], 2)

def get_literal(packet):
    b2 = ''
    i = 6
    more = True
    while more:
        more = packet[i] == '1'
        b2 += packet[i + 1 : i + 5]
        i += 5
    return int(b2, 2)

def get_length_type(packet):
    return int(packet[6], 2)

def get_length(packet, length_type):
    if not length_type:
        return int(packet[7:22], 2)
    else:
        return int(packet[7:18], 2)

    

def decode(hex):
    packet = hex_to_bin(hex)
    version = get_version(packet)
    type_id = get_type(packet)
    if type_id == 4:
        result = get_literal(packet)
    else:
        length_type = get_length_type(packet)
        length = get_length(packet, length_type)
        print(length_type, length)
        result = None
    
    print(hex, packet, version, type_id, result)
    return result


HEX = 'D2FE28'
HEX2 = '38006F45291200'
HEX3 = 'EE00D40C823060'


if __name__ == '__main__':
    decoded = decode(HEX)
    decoded = decode(HEX2)
    decoded = decode(HEX3)

