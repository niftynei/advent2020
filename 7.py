
"""
token: [{token:count},..]

[modifier color] bags contain ([count] [modifier color],|[no other]) bags.
"""

def bag_token_color(ln):
    idx = ln.find(' ', 0)
    idx = ln.find(' ', idx+1)
    return idx, ln[:idx]

def advance_containment(ln, idx):
    """ Strips "[modifier color] bags contain" """
    return ln[idx+14:]

def get_child(ln):
    idx = ln.find(' ', 0)
    tok = ln[:idx]
    if tok == 'no':
        return 0, None, 13

    count = int(tok)
    endx, tok = bag_token_color(ln[idx+1:])
    # trim the entire '[count] [modifier color] bag(s)'
    idx = idx + 1 + endx + 5
    # if there's only 1, then it'll say 'bag' not 'bags'
    if count == 1:
        idx -= 1
    return count, tok, idx

def load(filen):
    infos = {}
    with open(filen) as f:
        group = []
        lnn = 0
        for line in f:
            lnn += 1
            ln = line.strip('\n')
            idx, tok = bag_token_color(ln)
            ln = advance_containment(ln, idx)
            done = False
            while not done:
                count, tag, idx = get_child(ln)
                if tag:
                    group.append({'type': tag, 'count': count})
                ln = ln[idx:]
                if ln[0] == ',':
                    ln = ln[2:]
                else:
                    done = True
            infos[tok] = group
            group = []
    return infos

def dep_count(infos, tag):
    counter = 0
    visited = []
    dep_set = []
    dep_set.append(tag)
    while len(dep_set):
        tag = dep_set.pop(0)
        visited.append(tag)
        for k, v in infos.items():
            keys = [x['type'] for x in v]
            if tag in keys:
                if k not in dep_set and k != tag and k not in visited:
                    dep_set.append(k)
                    counter += 1
    return counter

def bag_count(infos, tag):
    dep_set = infos[tag]
    count = 0
    if len(dep_set):
        for bag in dep_set:
            tag = bag['type']
            val = bag['count']
            count += val + val * bag_count(infos, tag)
    return count

def run(infos, tag):
    return dep_count(infos, tag)
