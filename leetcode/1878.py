"""
1878. 矩阵中最大的三个菱形和
给你一个 m x n 的整数矩阵 grid 。

菱形和 指的是 grid 中一个正菱形 边界 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。


 

注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。

请你按照 降序 返回 grid 中三个最大的 互不相同的菱形和 。如果不同的和少于三个，则将它们全部返回。

 

示例 1：


输入：grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
输出：[228,216,211]
解释：最大的三个菱形和如上图所示。
- 蓝色：20 + 3 + 200 + 5 = 228
- 红色：200 + 2 + 10 + 4 = 216
- 绿色：5 + 200 + 4 + 2 = 211
示例 2：


输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：[20,9,8]
解释：最大的三个菱形和如上图所示。
- 蓝色：4 + 2 + 6 + 8 = 20
- 红色：9 （右下角红色的面积为 0 的菱形）
- 绿色：8 （下方中央面积为 0 的菱形）
示例 3：

输入：grid = [[7,7,7]]
输出：[7]
解释：所有三个可能的菱形和都相同，所以返回 [7] 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 105
通过次数2,449提交次数5,596
"""


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def get1(x, y, k):
            return pre1[x + k][y + k] - pre1[x][y]

        def get2(x, y, k):
            return pre2[x + k][y - k + 1] - pre2[x][y + 1]

        def update(v):
            if v in res:
                return
            heapq.heappush(res, v)
            if len(res) > 3:
                heapq.heappop(res)
        N, M = len(grid), len(grid[0])
        res = []
        pre1, pre2 = [[0] * (M + 1) for ii in range(N + 1)
                      ], [[0] * (M + 1) for ii in range(N + 1)]
        for ii, r in enumerate(grid):
            for jj, v in enumerate(r):
                pre1[ii + 1][jj + 1] = pre1[ii][jj] + v
                pre2[ii + 1][jj] = pre2[ii][jj + 1] + v
        for ii, r in enumerate(grid):
            for jj, v in enumerate(r):
                update(v)
                for k in range(1, min(ii + 1, N - ii, jj + 1, M - jj)):
                    a = get1(ii - k, jj, k)
                    b = get2(ii - k + 1, jj - 1, k - 1)
                    c = get1(ii, jj - k, k)
                    d = get2(ii, jj + k, k + 1)
                    update(a + b + c + d)
        return sorted([ii for ii in res if ii != 0], reverse=True)
