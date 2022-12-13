with open("day8.txt") as f:
    data = [[int(jj) for jj in ii.strip()] for ii in f.readlines()]


N, M = len(data), len(data[0])

def is_ok(x, y):
    if x in (0, N - 1) or y in (0, M - 1):
        return True
    return max(data[x][:y]) < data[x][y] or max(data[x][y + 1:]) < data[x][y] or max([data[ii][y] for ii in range(x)]) < data[x][y] or max([data[ii][y] for ii in range(x + 1, N)]) < data[x][y]

res = 0
for ii in range(N):
    for jj in range(M):
        if is_ok(ii, jj):
            res += 1

def get_num(x, y, dx, dy):
    
    ii, jj = x + dx, y + dy
    res = 1 if 0 <= ii < N and 0 <= jj < M else 0
    while 0 <= ii < N and 0 <= jj < M and data[ii][jj] < data[x][y]:
        ii, jj = ii + dx, jj + dy
        if 0 <= ii < N and 0 <= jj < M:
            res += 1
        
    return res

max_res = 0
for ii in range(N):
    for jj in range(M):
        res = 1
        for dx, dy in [(0,1), (1,0), (0,-1),(-1,0)]:
        
            res *= get_num(ii, jj, dx, dy)
        print(ii, jj, res)
        max_res = max(max_res, res)

