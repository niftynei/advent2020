from functools import cmp_to_key

""" return these sorted already """
def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            infos.append(line.strip(' \n'))
    return sorted(infos, key=cmp_to_key(compare_items))

def compare_items(item1, item2):
    for (c1, c2) in zip(item1, item2):
        if c1 == c2:
            continue
        if c1 == 'F':
            return -1
        if c1 == 'B':
            return 1
        if c1 == 'L':
            return -1
        if c1 == 'R':
            return 1
    return 0

def serial_to_row_col(serial):
    row = 0
    col = 0
    for i, t in enumerate(reversed(serial[:7])):
        v = 0
        if t == 'B':
            v = 1
        row |= v << i
    for i, t in enumerate(reversed(serial[7:])):
        v = 0
        if t == 'R':
            v = 1
        col |= v << i
    return row, col

def get_seat_id(serial):
    row, col = serial_to_row_col(serial)
    return row * 8 + col

def find_missing(infos):
    last_id = 0
    for i, inf in enumerate(infos):
        idx = get_seat_id(inf)
        if last_id != 0 and last_id != idx - 1:
            return idx - 1
        last_id = idx
    raise ValueError('unable to find seat')
