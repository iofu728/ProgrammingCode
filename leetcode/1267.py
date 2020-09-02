# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-01 17:34:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-01 17:34:44

"""
1267. Count Servers that Communicate Medium
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
Accepted 20,552 Submissions 35,573
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def countServers(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        g_l = {ii: [] for ii in range(N)}
        g_r = {ii: [] for ii in range(M)}
        res = 0
        for ii in range(N):
            for jj in range(M):
                if grid[ii][jj]:
                    g_l[ii].append(jj)
                    g_r[jj].append(ii)
        for k, v in g_l.items():
            if len(v) == 0:
                continue
            if len(v) > 1:
                res += len(v)
            else:
                if len(g_r[v[0]]) > 1:
                    res += 1
        # print(g_l, g_r)
        return res
