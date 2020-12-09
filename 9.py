def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            infos.append(int(line.strip('\n')))
    return infos


def preamble(infos, idx, size):
    return sorted(infos[idx-size:idx])

def find_sum(infos, pream, idx):
    size = len(pream)
    val = infos[idx]
    j_start = size - 1
    for i in range(size):
        for j in range(j_start, i, -1):
            sm = pream[i] + pream[j]
            if sm == val:
                return True
            if sm > val:
                continue
            j_start = j
            break
    return False

def run_1(infos, size):
    for i in range(len(infos[size:])):
        idx = i + size
        val = infos[idx]
        pream = preamble(infos, idx, size)
        if not find_sum(infos, pream, idx):
            return (idx, val)
    return (-1, -1)

def find_range(infos, idx):
    acc = 0
    start_range = 0
    target = infos[idx]
    for i in range(idx):
        acc += infos[i]
        if acc == target:
            return infos[start_range:i + 1]
        if acc < target:
            continue
        # acc > target, rollback from start
        while acc > target:
            acc -= infos[start_range]
            start_range += 1
            if acc == target:
                return infos[start_range:i + 1]
    return []

def run(infos, idx):
    ans = find_range(infos, idx)
    sans = sorted(ans)
    return sans[0] + sans[-1]
