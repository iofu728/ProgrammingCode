"""
1020. Number of Enclaves
Medium

931

29

Add to List

Share
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
Accepted
40,714
Submissions
66,370
"""


class Solution:
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            flag = x in [0, N - 1] or y in [0, M - 1]
            num = 1
            for dx, dy in self.DIRS:
                xx, yy = x + dx, y + dy
                if (
                    0 <= xx < N
                    and 0 <= yy < M
                    and grid[xx][yy] == 1
                    and self.flag[xx][yy] == 0
                ):
                    self.flag[xx][yy] = 1
                    f, k = dfs(xx, yy)
                    if f:
                        flag = True
                    num += k
            return flag, num

        N, M = len(grid), len(grid[0])
        self.flag = [[0] * M for _ in range(N)]
        res = 0
        for ii in range(N):
            for jj in range(M):
                if self.flag[ii][jj] == 0 and grid[ii][jj] == 1:
                    self.flag[ii][jj] = 1
                    f, k = dfs(ii, jj)
                    if not f:
                        res += k
        return res
