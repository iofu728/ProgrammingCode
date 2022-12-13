import functools

with open("day13.txt") as f:
    data = [ii.strip() for ii in f.readlines()]


def compare(a, b):
    if isinstance(a, int) and isinstance(b, list):
        a = [a]
    if isinstance(b, int) and isinstance(a, list):
        b = [b]
    for ii, jj in zip(a, b):
        if isinstance(ii, list) or isinstance(jj, list):
            x = compare(ii, jj)
            if x != 0:
                return x
        else:
            if ii > jj:
                return -1
            elif ii < jj:
                return 1
    if len(a) > len(b):
        return -1
    elif len(a) < len(b):
        return 1
    return 0

N = len(data)
res = 0
for ii in range(0, N, 3):
    l, r = eval(data[ii]), eval(data[ii + 1])
    if compare(l, r) == 1:
        print(l, r, ii // 3 + 1)
        res += (ii // 3 + 1)
    

xx = sorted([eval(ii) for ii in data if ii] + [[[2]], [[6]]], key=functools.cmp_to_key(compare), reverse=True)

(xx.index([[2]]) + 1) * (xx.index([[6]]) + 1)