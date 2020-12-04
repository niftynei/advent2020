"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
token_set = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
def token_index(token):
    c = 0
    for t in token_set:
        if token == t:
            return c
        c += 1
    raise ValueError("{} not found".format(token))


def load(filen):
    batch = []
    record = [None] * len(token_set)
    with open(filen) as f:
        last_return = False
        ln = 0
        for line in f:
            token_idx = 0
            val = []
            for c in line:
                if c == '\n':
                    if last_return:
                        batch.append(record)
                        record = [None] * len(token_set)
                    else:
                        if record[token_idx]:
                            raise ValueError('no no no, ln {}'.format(ln))
                        record[token_idx] = ''.join(val)
                        val = []
                    last_return = True
                elif c == ' ':
                    last_return = False
                    record[token_idx] = ''.join(val)
                    val = []
                    last_return = False
                elif c == ':':
                    token_idx = token_index(''.join(val))
                    val = []
                    last_return = False
                else:
                    val.append(c)
                    last_return = False
            ln += 1
        # save the last record
        batch.append(record)
    return batch

def test_1(record):
    return all(record[:len(token_set) - 1])

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
def test_2(record):
    if not test_1(record):
        return False

    # byr rules
    try:
        byr = int(record[0])
        if byr < 1920 or byr > 2002:
            # print('oops')
            return False
    except:
        # print('oops 1')
        return False

    # iyr rules
    try:
        iyr = int(record[1])
        if iyr < 2010 or iyr > 2020:
            # print('oops 2')
            return False
    except:
        # print('oops 3')
        return False

    # eyr rules
    try:
        eyr = int(record[2])
        if eyr < 2020 or eyr > 2030:
            # print('oops 4')
            return False
    except:
        # print('oops 5')
        return False

    # hgt
    hgt = record[3]
    if hgt.endswith('cm'):
        val = int(hgt[:-2])
        if val < 150 or val > 193:
            # print('oops 6')
            return False
    elif hgt.endswith('in'):
        val = int(hgt[:-2])
        if val < 59 or val > 76:
            # print('oops 7')
            return False
    else:
        # print('oops 8')
        return False

    # hcl
    hcl = record[4]
    if hcl[0] != '#':
        # print('oops 9')
        return False
    if len(hcl) != 7:
        # print('oops 10')
        return False
    for c in hcl[1:]:
        if c not in ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']:
            # print('oops 11')
            return False

    # ecl
    ecl = record[5]
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        # print('oops 12')
        return False

    # pid
    pid = record[6]
    if len(pid) != 9:
        # print('oops 13')
        return False
    try:
        int(pid)
    except:
        # print('oops 14')
        return False

    return True


def run(batch, valid_func):
    valids = 0
    for record in batch:
        if (valid_func(record)):
            valids += 1
    return valids

