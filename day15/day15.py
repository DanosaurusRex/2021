import heapq as hq

def read_input(filename):
    with open(filename) as f:
        grid = [[int(x) for x in line] for line in f.read().split()]
        return grid

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbours(grid, current):
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    x, y = current

    neighbours = []
    if x != 0:
        neighbours.append((x-1, y))
    if y != 0:
        neighbours.append((x, y-1))
    if x != max_x:
        neighbours.append((x+1, y))
    if y != max_y:
        neighbours.append((x, y+1))
    return neighbours

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path

def a_star(grid, start, end):
    open_set = [(0, start)]
    hq.heapify(open_set)
    came_from = {}

    g_score = {}
    f_score = {}
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            g_score[(x, y)] = float('inf')
            f_score[(x, y)] = float('inf')
    
    g_score[start] = 0
    f_score[start] = h(start, end)

    while open_set:
        _, current = hq.heappop(open_set)

        if current == end:
            path = reconstruct_path(came_from, current)
            return path
        
        for neighbour in get_neighbours(grid, current):
            n_x, n_y = neighbour
            temp_g_score = g_score[current] + grid[n_y][n_x]

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour, end)
                if neighbour not in open_set:
                    hq.heappush(open_set, (f_score[neighbour], neighbour))
    
    print('No path found.')
    return False

def score_path(grid, path):
    return sum([grid[y][x] for x, y in path])

def part1(grid):
    start = (0, 0)
    end_x = len(grid[0]) - 1
    end_y = len(grid) - 1
    end = (end_x, end_y)

    path = a_star(grid, start, end)
    score = score_path(grid, path)

    print(f'Part 1: {score}')

def extend_grid(grid, factor=5):
    new_grid = []
    for row in grid:
        new_row = []
        for i in range(factor):
            for val in row:
                new_val = val + i
                if new_val > 9:
                    new_val -= 9
                new_row.append(new_val)
        new_grid.append(new_row)

    copy = new_grid.copy()
    for i in range(1, factor):
        for row in copy:
            new_row = []
            for val in row:
                new_val = val + i
                if new_val > 9:
                    new_val -= 9
                new_row.append(new_val)
            new_grid.append(new_row)
    
    return new_grid


def part2(grid):
    grid = extend_grid(grid)

    start = (0, 0)
    end_x = len(grid[0]) - 1
    end_y = len(grid) - 1
    end = (end_x, end_y)

    path = a_star(grid, start, end)
    score = score_path(grid, path)

    print(f'Part 2: {score}')


if __name__ == '__main__':
    grid = read_input('day15/input.txt')
    part1(grid)
    part2(grid)
    