def read_input(filename) -> list:
    boards = []
    with open(filename) as f:
        numbers = [int(n) for n in f.readline().split(",")]
        board = []
        for line in f.readlines():
            if line.strip():
                board.append([int(n) for n in line.split()])
            else:
                if board:
                    boards.append(board)
                board = []
        return numbers, boards


def part1(numbers, boards):
    winner = None
    win_num = None

    for i, _ in enumerate(numbers):
        nums = set(numbers[: i + 1])

        for board in boards:
            if winner:
                break

            # horizontal
            for line in board:
                if not set(line) - nums:
                    winner = board
                    win_num = numbers[i]
                    break

            # vertical
            for j, _ in enumerate(board[0]):
                line = [row[j] for row in board]
                if not set(line) - nums:
                    winner = board
                    win_num = numbers[i]
                    break

            if winner:
                break
        if winner:
            break

    win_list = [x for row in winner for x in row if x not in nums]

    print("Part 1:", sum(win_list) * win_num)


def part2(numbers, boards):
    loser = None
    lose_num = None

    boards = boards.copy()

    for i, _ in enumerate(numbers):
        nums = set(numbers[: i + 1])

        if len(boards) > 1:
            for board in boards.copy():
                if board not in boards:
                    continue

                # horizontal
                for line in board:
                    if not set(line) - nums:
                        boards.remove(board)
                        break

                if board not in boards:
                    continue

                # vertical
                for j, _ in enumerate(board[0]):
                    line = [row[j] for row in board]
                    if not set(line) - nums:
                        boards.remove(board)
                        break
        else:
            loser = boards[0]

            # horizontal
            for line in board:
                if not set(line) - nums:
                    lose_num = numbers[i]
                    break

            # vertical
            for j, _ in enumerate(board[0]):
                line = [row[j] for row in board]
                if not set(line) - nums:
                    lose_num = numbers[i]
                    break

        if lose_num:
            break

    lose_list = [x for row in loser for x in row if x not in nums]

    print("Part 2:", sum(lose_list) * lose_num)


if __name__ == "__main__":
    numbers, boards = read_input("day4/input.txt")

    part1(numbers, boards)
    part2(numbers, boards)
