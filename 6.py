import string

def load(filen):
    infos = []
    group = []
    with open(filen) as f:
        for line in f:
            ln = line.strip('\n')
            if len(ln) == 0:
                infos.append(group)
                group = []
                continue
            group.append(ln)
        # don't forget the last one
        infos.append(group)
    return infos

def group_uniq(infos):
    count = 0
    for g in infos:
        found = [0] * 26
        for p in g:
            for c in p:
                idx = string.ascii_lowercase.index(c)
                if found[idx] == 0:
                    count += 1
                found[idx] += 1
    return count

def group_all(infos):
    count = 0
    for g in infos:
        found = [0] * 26
        for p in g:
            for c in p:
                idx = string.ascii_lowercase.index(c)
                found[idx] += 1
        for x in found:
            if x == len(g):
                count += 1
    return count
