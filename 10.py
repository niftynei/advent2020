def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            infos.append(int(line.strip('\n')))
    # go ahead and sort and add the start/end
    infos.sort()
    return [0] + infos + [infos[-1] + 3]


def count_diff(infos):
    counts = [0] * 3
    for i, j in enumerate(infos):
        if i == 0:
            continue
        else:
            last = infos[i - 1]

        counts[(j - last) - 1] += 1
    return counts

def count_runs(infos):
    counts = [0] * len(infos)
    for i, j in enumerate(infos):
        if i < 2:
            counts[i] = 1
            continue
        counts[i] = counts[i-1]
        if j - infos[i-2] <= 3:
            counts[i] += counts[i-2]
        if i < 3:
            continue
        if j - infos[i-3] <= 3:
            counts[i] += counts[i-3]

    return counts[-1]

def print_perms(infos, i):
    if i == len(infos) - 1:
        return 1

    a = b = c = 0
    if i + 1 < len(infos):
        if infos[i+1] <= infos[i] + 3:
            a = print_perms(infos, i+1)
    if i + 2 < len(infos):
        if infos[i+2] <= infos[i] + 3:
            b = print_perms(infos, i+2)
    if i + 3 < len(infos):
        if infos[i+3] <= infos[i] + 3:
            c = print_perms(infos, i+3)

    return a + b + c
