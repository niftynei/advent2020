def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            ln = line.strip('\n')
            tok = ln[:3]
            if ln[4] == '+':
                val = int(ln[5:])
            else:
                val = int(ln[4:])
            infos.append({'inst': tok, 'val': val})
    return infos

def exec_count(infos, flip_idx):
    ran = [False] * len(infos)
    size = len(infos)
    idx = 0
    acc = 0
    while idx < size and not ran[idx]:
        inst = infos[idx]
        ran[idx] = True
        ex = inst['inst']

        if idx == flip_idx:
            if ex == 'nop':
                ex = 'jmp'
            elif ex == 'jmp':
                ex = 'nop'

        if ex == 'acc':
            acc += inst['val']
            idx += 1
        elif ex == 'nop':
            idx += 1
        elif ex == 'jmp':
            idx += inst['val']

    return acc, idx >= size

def idx_list(infos,inst):
    ans = []
    for i, x in enumerate(infos):
        if x['inst'] == inst:
            ans.append(i)
    return ans


def flip_inst(infos, inst):
    insts = idx_list(infos, inst)
    for inst_idx in insts:
        acc, term = exec_count(infos, inst_idx)
        if term:
            return acc
    return -1
