def read_input(filename):
    template = ''
    rules = {}
    with open(filename) as f:
        template = f.readline().strip()
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            pair, insert = line.split(' -> ')
            rules[pair] = insert
    return template, rules

def count_chars(sequence):
    counts = {}
    for char in set(sequence):
        counts[char] = sequence.count(char)
    return counts

def count_pairs(sequence):
    pair_counts = {}
    for i, _ in enumerate(sequence[:-1]):
        pair = sequence[i:i+2]
        if pair not in pair_counts:
            pair_counts[pair] = 0
        pair_counts[pair] += 1
    return pair_counts

def polymerise(template, rules, runs):
    pairs = count_pairs(template)
    chars = count_chars(template)
    for run in range(runs):
        new_pairs = pairs.copy()
        for pair, qty in pairs.items():
            inserted = rules.get(pair, '')
            if not qty or not inserted:
                continue

            first = pair[0] + inserted
            second = inserted + pair[1]

            for new_pair in (first, second):
                if new_pair not in new_pairs:
                    new_pairs[new_pair] = 0
                new_pairs[new_pair] += qty
            new_pairs[pair] -= qty
            
            if inserted not in chars:
                chars[inserted] = 0
            chars[inserted] += qty

        pairs = new_pairs
    return chars

def part1(template, rules):
    chars = polymerise(template, rules, runs=10)
    cleaned_chars = {k: v for k, v in chars.items() if v}
    answer = max(cleaned_chars.values()) - min(cleaned_chars.values())
    print(f'Part 1: {answer}')

def part2(template, rules):
    chars = polymerise(template, rules, runs=40)
    cleaned_chars = {k: v for k, v in chars.items() if v}
    answer = max(cleaned_chars.values()) - min(cleaned_chars.values())
    print(f'Part 2: {answer}')


if __name__ == '__main__':
    template, rules = read_input('day14/input.txt')
    part1(template, rules)
    part2(template, rules)
