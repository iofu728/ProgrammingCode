from functools import lru_cache
with open("day12.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

N, M = len(data), len(data[0])
sx, sy = -1, -1
ex, ey = -1, -1
for ii in range(N):
    for jj in range(M):
        if data[ii][jj] == "S":
            sx, sy = ii, jj
        if data[ii][jj] == "E":
            ex, ey = ii, jj

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def is_ok(x, y, px, py):
    if not(0 <= x < N and 0 <= y < M):
        return False
    if data[px][py] == "S":
        return data[x][y] == "a"
    if data[px][py] == "z":
        return data[x][y] == "E" or (data[x][y].islower() and data[x][y] <= data[px][py])
    return data[x][y] ==  chr(ord(data[px][py]) + 1) or (data[x][y].islower() and data[x][y] <= data[px][py])

res = 10**9 + 7
done = [[-1] * M for _ in range(N)]

# done[sx][sy] = 1
q = [(0, sx, sy)]

while q:
    d, x, y = heapq.heappop(q)
    if x == ex and y == ey:
        res = d
        break
    if done[x][y] == 1:
        continue
    done[x][y] = 1
    print(x, y, data[x][y], d)
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M) or done[nx][ny] != -1:
            continue
        if is_ok(nx, ny, x, y):
            heapq.heappush(q, (d + 1, nx, ny))
            # q.append((nx, ny, d + 1))


def is_ok(x, y, px, py):
    if not(0 <= x < N and 0 <= y < M):
        return False
    if data[px][py] == "E":
        return data[x][y] == "z"
    return data[x][y] ==  chr(ord(data[px][py]) - 1) or (data[x][y].islower() and data[x][y] >= data[px][py])

res = 10**9 + 7
done = [[-1] * M for _ in range(N)]

# done[sx][sy] = 1
q = [(0, ex, ey)]

while q:
    d, x, y = heapq.heappop(q)
    if data[x][y] == "a":
        res = d
        break
    if done[x][y] == 1:
        continue
    done[x][y] = 1
    print(x, y, data[x][y], d)
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M) or done[nx][ny] != -1:
            continue
        if is_ok(nx, ny, x, y):
            heapq.heappush(q, (d + 1, nx, ny))
            # q.append((nx, ny, d + 1))

