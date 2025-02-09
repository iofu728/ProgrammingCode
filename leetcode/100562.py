"""
100562. 按对角线进行矩阵排序 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个大小为 n x n 的整数方阵 grid。返回一个经过如下调整的矩阵：

左下角三角形（包括中间对角线）的对角线按 非递增顺序 排序。
右上角三角形 的对角线按 非递减顺序 排序。
 

示例 1：

输入： grid = [[1,7,3],[9,8,2],[4,5,6]]

输出： [[8,2,3],[9,6,7],[4,5,1]]

解释：



标有黑色箭头的对角线（左下角三角形）应按非递增顺序排序：

[1, 8, 6] 变为 [8, 6, 1]。
[9, 5] 和 [4] 保持不变。
标有蓝色箭头的对角线（右上角三角形）应按非递减顺序排序：

[7, 2] 变为 [2, 7]。
[3] 保持不变。
示例 2：

输入： grid = [[0,1],[1,2]]

输出： [[2,1],[1,0]]

解释：



标有黑色箭头的对角线必须按非递增顺序排序，因此 [0, 2] 变为 [2, 0]。其他对角线已经符合要求。

示例 3：

输入： grid = [[1]]

输出： [[1]]

解释：

只有一个元素的对角线已经符合要求，因此无需修改。

 

提示：

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105
"""

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N, M = len(grid), len(grid[0])
        for k in range(-(M - 1), N):
            tmp = []
            for i in range(0, N):
                j = i - k
                # print(i, j, k)
                if not (0 <= j <= M - 1):
                    continue
                tmp.append(grid[i][j])
            if k >= 0:
                tmp = sorted(tmp, reverse=True)
            else:
                tmp = sorted(tmp)
            # print(k, tmp)
            y = 0
            for i in range(0, N):
                j = i - k
                if not 0 <= j <= M - 1:
                    continue
                grid[i][j] = tmp[y]
                y += 1
        return grid
