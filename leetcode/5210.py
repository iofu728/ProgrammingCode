# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-27 11:41:04
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-27 11:52:00

"""
5210. 球会落何处 显示英文描述 
通过的用户数801
尝试过的用户数903
用户总通过次数806
用户总提交次数1555
题目难度Medium
用一个大小为 m x n 的二维网格 grid 表示一个箱子。你有 n 颗球。箱子的顶部和底部都是开着的。

箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。

将球导向右侧的挡板跨过左上角和右下角，在网格中用 1 表示。
将球导向左侧的挡板跨过右上角和左下角，在网格中用 -1 表示。
在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。如果球恰好卡在两块挡板之间的 "V" 形图案，或者被一块挡导向到箱子的任意一侧边上，就会卡住。

返回一个大小为 n 的数组 answer ，其中 answer[i] 是球放在顶部的第 i 列后从底部掉出来的那一列对应的下标，如果球卡在盒子里，则返回 -1 。

 

示例 1：



输入：grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
输出：[1,-1,-1,-1,-1]
解释：示例如图：
b0 球开始放在第 0 列上，最终从箱子底部第 1 列掉出。
b1 球开始放在第 1 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。
b2 球开始放在第 2 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
b3 球开始放在第 3 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
b4 球开始放在第 4 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。
示例 2：

输入：grid = [[-1]]
输出：[-1]
解释：球被卡在箱子左侧边上。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] 为 1 或 -1
"""


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def dfs(x):
            # print("===", x)
            y = 0
            while True:
                # print(x, y)
                if y == M:
                    return x
                if (x == N - 1 and grid[y][x] == 1) or (x == 0 and grid[y][x] == -1):
                    return -1
                if x - 1 < N and grid[y][x] == 1 and grid[y][x + 1] == 1:
                    x += 1
                    y += 1
                elif x > 0 and grid[y][x] == -1 and grid[y][x - 1] == -1:
                    x -= 1
                    y += 1
                else:
                    return -1

        M, N = len(grid), len(grid[0])
        return [dfs(ii) for ii in range(N)]
