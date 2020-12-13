def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            infos.append(line.strip('\n'))
    return infos


move_set = [(0,1),(1,0),(0,-1),(-1,0)]

""" current (x,y) """
def update_face(cur_idx, inst):
    val = int(inst[1:])
    mod = 1 if inst[0] == 'R' else -1
    move = val // 90 * mod

    return (cur_idx + move) % len(move_set)

def cardinal_to_move_idx(c):
    if c == 'N':
        return 0
    if c == 'E':
        return 1
    if c == 'S':
        return 2
    return 3

def abv(val):
    if val >= 0:
        return val
    return val * -1

def rotate_waypoint(waypt, d):
    val = int(d[1:])
    if val == 180:
        return [ -1 * waypt[0], -1 * waypt[1]]

    if (val == 90 and d[0] == 'L') or (val == 270 and d[0] == 'R'):
        update = [-1 * waypt[1], waypt[0]]
        print("updating waypt!", waypt, update)
        return update

    return [waypt[1], -1 * waypt[0]]

def run(infos):
    waypt = [10, 1]
    coord = [0,0]
    for d in infos:
        if d[0] == 'F':
            val = int(d[1:])
            coord[0] += val * waypt[0]
            coord[1] += val * waypt[1]
            print(waypt, coord)
            continue

        if d[0] == 'L' or d[0] == 'R':
            waypt = rotate_waypoint(waypt, d)
            print(waypt, coord)
            continue

        direction = cardinal_to_move_idx(d[0])
        val = int(d[1:])
        waypt[0] += val * move_set[direction][0]
        waypt[1] += val * move_set[direction][1]
        print(waypt, coord)

    return coord, abv(coord[0]) + abv(coord[1])

def run_test():
    test = load('day12_test.txt')
    run(test)
