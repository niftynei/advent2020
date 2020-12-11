def load(filen):
    grid = []
    with open(filen) as f:
        for row in f:
            row = row.strip('\n')
            cols = []
            for c in row:
                if c == 'L':
                    cols.append(False)
                else:
                    cols.append(None)
            grid.append(cols)
    return grid

def copy_grid(grid):
    return [ x.copy() for x in grid ]


def find_seat(grid, start_at, inc):
    i, j = start_at
    col_size = len(grid)
    row_size = len(grid[0])

    x = j
    y = i
    while True:
        x += inc[0]
        y += inc[1]
        if x < 0 or x == row_size:
            return None
        if y < 0 or y == col_size:
            return None

        if grid[y][x] is not None:
            return (x, y)

"""
We pre-compute the coordinates of each seat in any direction,
for each seat, and save a range for it.
"""
def compute_ranges(grid):
    check_range = [(0,1), (1,0), (1,1), (-1,1), (1,-1),(0,-1),(-1,0),(-1,-1)]
    ranges = [[] for x in grid]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            spot_range = []

            if col is None:
                ranges[i].append(spot_range)
                continue

            for r in check_range:
                pair = find_seat(grid, (i,j), r)
                if pair:
                    spot_range.append(pair)

            ranges[i].append(spot_range)
    return ranges



def update_grid(grid, range_grid):
    col_size = len(grid)
    row_size = len(grid[0])
    result = copy_grid(grid)
    count = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            # Ignore floor spaces
            if col is None:
                continue

            occupied = 0
            empty = 0
            # We use our pre-computed coordinates of
            # 'viewable' seats to figure out who to
            # check for 'flippability'
            check_range = range_grid[i][j]
            for r in check_range:
                x = r[0]
                y = r[1]
                if grid[y][x] is True:
                    occupied += 1
                elif grid[y][x] is False:
                    empty += 1

            if col is True and occupied >= 5:
                result[i][j] = False
                count += 1
            elif col is False and occupied == 0:
                result[i][j] = True
                count += 1

    return result, count

def update_til_stasis(grid):
    range_grid = compute_ranges(grid)
    count = 1
    while count != 0:
        grid, count = update_grid(grid, range_grid)

    return grid

def count_occupied(grid):
    count = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col is True:
                count += 1
    return count

"""
to run:
    grid = load('day11.txt')
    b = update_til_stasis(grid)
    count_occupied(b)
"""
