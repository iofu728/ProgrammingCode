# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2019-11-23 11:38:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2019-11-23 12:14:23

from sys import stdin


def get_stdin():
    return [int(ii) for ii in stdin.readline().strip().split()]
m, n = get_stdin()
matrix = get_stdin()
matrix = [[matrix[ii * n + jj] for jj in range(n)]for ii in range(m)]

max_price = -1

def dfs(line_id: int, row1: int, row2: int, now: int):
    global max_price
    if row1 == row2:
        return
    if row1 >= n or row1 < 0:
        return
    if row2 >= n or row2 < 0:
        return
    if m - line_id < row1 - 1 or m - line_id < (n - row2 - 1):
        return
           
    if line_id >= m:
        if row1 != 0 or row2 != n -1:
            return
        if now > max_price:
            max_price = now
        return
    if row1 > 0:
        if row2 > 0:
            dfs(line_id + 1, row1 - 1, row2 - 1, now + matrix[line_id][row1 - 1] + matrix[line_id][row2 - 1])
        dfs(line_id + 1, row1 - 1, row2, now + matrix[line_id][row1 - 1] + matrix[line_id][row2])
        if row2 < n - 1:
            dfs(line_id + 1, row1 - 1, row2 + 1, now + matrix[line_id][row1 - 1] + matrix[line_id][row2 + 1])
    if row2 > 0:
        dfs(line_id + 1, row1, row2 - 1, now + matrix[line_id][row1] + matrix[line_id][row2 - 1])
    dfs(line_id + 1, row1, row2, now + matrix[line_id][row1] + matrix[line_id][row2])
    if row2 < n - 1:
        dfs(line_id + 1, row1, row2 + 1, now + matrix[line_id][row1] + matrix[line_id][row2 + 1])
    if row1 < n -1:
        if row2 > 0:
            dfs(line_id + 1, row1 + 1, row2 - 1, now + matrix[line_id][row1 + 1] + matrix[line_id][row2 - 1])
        dfs(line_id + 1, row1 + 1, row2, now + matrix[line_id][row1 + 1] + matrix[line_id][row2])
        if row2 < n - 1:
            dfs(line_id + 1, row1 + 1, row2 + 1, now + matrix[line_id][row1 + 1] + matrix[line_id][row2 + 1])
    


def main():
    if n < 2:
        print(-1)
        return
    dfs(1, 0, n - 1, matrix[0][0] + matrix[0][n - 1])
    print(max_price)

main()

