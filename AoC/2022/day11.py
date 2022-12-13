'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''

with open("day11.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

now  = []
g = []
for ii in range(0, len(data), 7):
    items = [int(jj) for jj in data[ii + 1].replace("Starting items: ", "").split(", ")]
    op = data[ii + 2].replace("Operation: new = ", "")
    dv = int(data[ii + 3].replace("Test: divisible by ", ""))
    a, b = int(data[ii + 4].replace("If true: throw to monkey ", "")), int(data[ii + 5].replace("If false: throw to monkey ", ""))
    g.append((op, dv, a, b))
    now.append(items)

m_times = [0] * len(g)

MOD = 13 * 2 * 19 * 11 * 7 * 5 * 3 * 17 * 23

for _ in range(10000):
    for ii in range(len(g)):
        op, dv, a, b = g[ii]
        while now[ii]:
            old = now[ii].pop(0)
            m_times[ii] += 1
            ne = eval(op)
            # ne //= 3
            ne %= MOD
            if ne % dv == 0:
                now[a].append(ne)
            else:
                now[b].append(ne)
    print(_)


