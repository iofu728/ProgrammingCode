# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-05 15:50:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-05 16:09:58

"""
4. 变换的迷宫
通过的用户数8
尝试过的用户数32
用户总通过次数8
用户总提交次数72
题目难度Hard
某解密游戏中，有一个 N*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 (n-1,m-1) 位置。迷宫变化规律记录于 maze 中，maze[i] 表示 i 时刻迷宫的地形状态，"." 表示可通行空地，"#" 表示陷阱。

地形图初始状态记作 maze[0]，此时小力位于起点 (0,0)。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。

小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：

临时消除术：将指定位置在下一个时刻变为空地；
永久消除术：将指定位置永久变为空地。
请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？

注意： 输入数据保证起点和终点在所有时刻均为空地。

示例 1：

输入：maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]

输出：true

解释：
maze.gif

示例 2：

输入：maze = [[".#.","..."],["...","..."]]

输出：false

解释：由于时间不够，小力无法到达终点逃出迷宫。

示例 3：

输入：maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]

输出：false

解释：由于道路不通，小力无法到达终点逃出迷宫。

提示：

1 <= maze.length <= 100
1 <= maze[i].length, maze[i][j].length <= 50
maze[i][j] 仅包含 "."、"#"
"""


class Solution:
    DIRS = [(0, 1), (1, 0)]

    def escapeMaze(self, maze: List[List[str]]) -> bool:
        def get_father(r, p):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p

        N, M = len(maze), len(maze[0])
        r = list(range(N * M))
        for ii in range(N):
            for jj in range(M):
                a = ii * M + jj
                if maze[ii][jj] == ".":
                    if jj + 1 < M and maze[ii][jj + 1] == ".":
                        b = ii * M + jj + 1
                        ra, rb = get_father(r, a), get_father(r, b)
                        if ra != rb:
                            r[rb] = ra
                    if ii + 1 < N and maze[ii + 1][jj] == ".":
                        b = (ii + 1) * M + jj
                        ra, rb = get_father(r, a), get_father(r, b)
                        if ra != rb:
                            r[rb] = ra
        for ii in range(N):
            print([get_father(r, ii * M + jj) for jj in range(M)])
        if get_father(r, 0) == get_father(r, N * M - 1):
            return True
