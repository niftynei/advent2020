"""
Load this file
    >>> exec(open('2.py').read())

Load the challenge input
    >>> info = load('day2.txt')

Solve the first puzzle
    >>> run(info, policy_1)

Solve the second puzzle
    >>> run(info, policy_2)

"""

def policy_1(target, mn, mx, inp):
    count = 0
    for c in inp:
        if c == target:
            count += 1
    return count >= mn and count <= mx


def policy_2(target, mn, mx, inp):
    return (inp[mn + 1] == target) ^ (inp[mx + 1] == target)

def run(inp, policy):
    matches = 0
    for p in inp:
        mn = 0
        mx = 0
        target = ''
        toks = []
        index = 0
        for c in p:
            if c in ['1','2','3','4','5','6','7','8','9','0']:
                toks.append(c)
            elif c == '-':
                mn = int(''.join(toks))
                toks = []
            elif c == ' ':
                mx = int(''.join(toks))
                toks = []
            elif c == ':':
                target = toks[-1]
                break
            else:
                toks.append(c)
            index += 1

        if policy(target, mn, mx, p[index:]):
            matches += 1

    return matches


def load(filen):
    infos = []
    with open(filen) as f:
        for line in f:
            infos.append(line.strip(' \n'))
    return infos
