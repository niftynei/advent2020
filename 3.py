def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            infos.append(line.strip(' \n'))
    return infos

def run_inner(inp, col_inc, row_inc):
    index = 0
    total = 0
    for tree_idx in range(0, len(inp), row_inc):
        trees = inp[tree_idx]
        at = index % len(trees)
        if trees[at] == '#':
            total += 1
        index += col_inc
    return total

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
def run(inp):
    runs = [(1,1),
            (3,1),
            (5,1),
            (7,1),
            (1,2)]

    acc = 1
    for run in runs:
        c = run_two(inp, run[0], run[1])
        print(c)
        acc *= c
    return acc
