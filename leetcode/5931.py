"""
5931. 用邮票贴满网格图 显示英文描述 
User Accepted:2
User Tried:4
Total Accepted:2
Total Submissions:6
Difficulty:Hard
给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

覆盖所有 空 格子。
不覆盖任何 被占据 的格子。
我们可以放入任意数目的邮票。
邮票可以相互有 重叠 部分。
邮票不允许 旋转 。
邮票必须完全在矩阵 内 。
如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。

 

示例 1：



输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
输出：true
解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
示例 2：



输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
输出：false 
解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
 

提示：

m == grid.length
n == grid[r].length
1 <= m, n <= 105
1 <= m * n <= 2 * 105
grid[r][c] 要么是 0 ，要么是 1 。
1 <= stampHeight, stampWidth <= 105
"""
class Solution:
    KK = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        @lru_cache(None)
        def is_ok_single(x, y, idx):
            dx1, dy1, dx2, dy2 = DIRS[idx]
            x1, y1, x2, y2 = dx1 + x, dy1 + y, dx2 + x, dy2 + y
            # print(x1, x2, y1, y2)
            if not (0 <= x1 < N and 0 <= y1 < M and 0 <= x2 < N and 0 <= y2 < M):
                return False
            l, r = bisect.bisect_left(point, (x1, y1)), bisect.bisect_left(point, (x2, y2))
            for k in range(l, min(r + 1, K)):
                xx, yy = point[k]
                if x1 <= xx <= x2 and y1 <= yy <= y2:
                    return False
            bisect.insort(fin, (x1, y1))
            return True
        
        @lru_cache(None)
        def is_ok(x, y):
            if not (0 <= x < N and 0 <= y < M) or (x, y) in ks:
                return True
            for ii in range(4):
                if is_ok_single(x, y, ii):
                    return True
            if fin:
                k = bisect.bisect_left(fin, (x, y))
                if k > 0:
                    x1, y1 = fin[k - 1]
                    if x1 + stampHeight - 1 >= x and y1 + stampWidth - 1 >= y:
                        return True
            return False
            
        N, M = len(grid), len(grid[0])
        point = []
        for ii in range(N):
            for jj in range(M):
                if grid[ii][jj] == 1:
                    point.append((ii, jj))
        if len(point) != N * M and (stampHeight > N or stampWidth > M):
            return False
        fin = []
        ks = set(point)
        K = len(point)           
        DIRS = [(-stampHeight + 1, 0, 0, stampWidth - 1), (0, 0, stampHeight - 1, stampWidth - 1), (0, -stampWidth + 1, stampHeight - 1, 0), (-stampHeight + 1, -stampWidth + 1, 0, 0)]

        for ii, jj in point:
            for dx, dy in self.KK:
                if is_ok(ii + dx, jj + dy) == False:
                    return False
        return True
