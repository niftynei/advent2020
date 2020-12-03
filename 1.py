
def run(invs):
    for i in range(len(invs)):
            for j in range(len(invs)-1,0,-1):
                if i >= j:
                    break
                sm = invs[i] + invs[j]
                if sm >= 2020:
                    continue
                if 2020 - sm > invs[j]:
                    start = j
                    end = len(invs)
                elif 2020 - sm < invs[i]:
                    start = 0
                    end = i
                else:
                    start = i
                    end = j
                for k in range(start, end):
                    ss = sm + invs[k]
                    if ss == 2020:
                        return (invs[i],
                                invs[j],
                                invs[k],
                                invs[i] * invs[j] * invs[k])
                    if ss > 2020:
                        break

