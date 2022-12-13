with open("day10.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

x, y = 1, 0
target = 20



res = []
for ii in data:
    if ii == "noop":
        if is_ok(y, y + 1):
            res.append(x)
            target += 40
        y += 1
    else:
        z = int(ii[5:])
        if is_ok(y, y + 2):
            res.append(x)
            target += 40
        x += z
        y += 2

while y < 220:
    res.extend([x] * (220 - target)//40)
sum([ii * jj for ii, jj in zip(res, [20, 60, 100, 140, 180, 220])])


res = []
def get_str(x, now):
    if now in [x - 1, x, x + 1]:
        return "#"
    return "."
for ii in data:
    res.append(get_str(x, y))
    if ii == "noop":
        y += 1
    else:
        z = int(ii[5:])
        res.append(get_str(x, y + 1))
        x += z
        y += 2
    y %= 40