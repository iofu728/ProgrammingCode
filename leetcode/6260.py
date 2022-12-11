"""
6260. 矩阵查询可获得的最大分数 显示英文描述 
通过的用户数234
尝试过的用户数373
用户总通过次数255
用户总提交次数550
题目难度Hard
给你一个大小为 m x n 的整数矩阵 grid 和一个大小为 k 的数组 queries 。

找出一个大小为 k 的数组 answer ，且满足对于每个整数 queres[i] ，你从矩阵 左上角 单元格开始，重复以下过程：

如果 queries[i] 严格 大于你当前所处位置单元格，如果该单元格是第一次访问，则获得 1 分，并且你可以移动到所有 4 个方向（上、下、左、右）上任一 相邻 单元格。
否则，你不能获得任何分，并且结束这一过程。
在过程结束后，answer[i] 是你可以获得的最大分数。注意，对于每个查询，你可以访问同一个单元格 多次 。

返回结果数组 answer 。

 

示例 1：


输入：grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
输出：[5,8,1]
解释：上图展示了每个查询中访问并获得分数的单元格。
示例 2：


输入：grid = [[5,2,1],[1,1,2]], queries = [3]
输出：[0]
解释：无法获得分数，因为左上角单元格的值大于等于 3 。
 

提示：

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106
"""
class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        q = [[grid[0][0], 0, 0]]
        d = {}
        cnt = Counter()
        while q:
            dis, x, y = heappop(q)
            if (x, y) not in d:
                d[x, y] = dis
                cnt[dis] += 1
                for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        heappush(q, [max(dis, grid[nx][ny]), nx, ny])
        for i in range(1, 10**6 + 1):
            cnt[i] = cnt[i] + cnt[i-1]
        return [cnt[a-1] for a in queries]
                    
                
            
        