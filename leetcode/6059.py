"""
6059. 检查是否有合法括号字符串路径 显示英文描述 
通过的用户数322
尝试过的用户数692
用户总通过次数353
用户总提交次数1137
题目难度Hard
一个括号字符串是一个 非空 且只包含 '(' 和 ')' 的字符串。如果下面 任意 条件为 真 ，那么这个括号字符串就是 合法的 。

字符串是 () 。
字符串可以表示为 AB（A 连接 B），A 和 B 都是合法括号序列。
字符串可以表示为 (A) ，其中 A 是合法括号序列。
给你一个 m x n 的括号网格图矩阵 grid 。网格图中一个 合法括号路径 是满足以下所有条件的一条路径：

路径开始于左上角格子 (0, 0) 。
路径结束于右下角格子 (m - 1, n - 1) 。
路径每次只会向 下 或者向 右 移动。
路径经过的格子组成的括号字符串是 合法 的。
如果网格图中存在一条 合法括号路径 ，请返回 true ，否则返回 false 。

 

示例 1：



输入：grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
输出：true
解释：上图展示了两条路径，它们都是合法括号字符串路径。
第一条路径得到的合法字符串是 "()(())" 。
第二条路径得到的合法字符串是 "((()))" 。
注意可能有其他的合法括号字符串路径。
示例 2：



输入：grid = [[")",")"],["(","("]]
输出：false
解释：两条可行路径分别得到 "))(" 和 ")((" 。由于它们都不是合法括号字符串，我们返回 false 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] 要么是 '(' ，要么是 ')' 。
"""


class Solution:
    DIRS = [(0, 1), (1, 0)]

    def hasValidPath(self, grid: List[List[str]]) -> bool:
        @lru_cache(None)
        def dfs(x, y, now):
            if (x, y) == (N - 1, M - 1):
                if now == 0:
                    self.res = True
                return
            if self.res:
                return
            # if x >= N // 2 + 1 or  y>= M // 2 + 1:
            #     c[(x, y)].add(now)
            #     return
            for dx, dy in self.DIRS:
                xx, yy = dx + x, dy + y
                if 0 <= xx < N and 0 <= yy < M and now + (1 if grid[xx][yy] == "(" else - 1) >= 0:
                    # done.add((xx, yy))
                    dfs(xx, yy, now + (1 if grid[xx][yy] == "(" else - 1))
                    # done.remove((xx, yy))

        # @lru_cache(None)
        # def dfs2(x, y, now):
        #     if self.res:
        #         return
        #     if x < N // 2 or  y< M // 2:
        #         return
        #     for dx, dy in self.DIRS:
        #         xx, yy = -dx + x, -dy + y
        #         # print(xx, yy, now + (1 if grid[xx][yy] == ")" else - 1), (xx, yy) not in done)
        #         if 0 <= xx < N and 0 <= yy < M and now + (1 if grid[xx][yy] == ")" else - 1) >= 0:
        #             if now in c[(xx, yy)]:
        #                 self.res = True
        #                 return
        #             # done.add((xx, yy))
        #             dfs2(xx, yy, now + (1 if grid[xx][yy] == ")" else - 1))
        #             # done.remove((xx, yy))

        N, M = len(grid), len(grid[0])
        c = defaultdict(set)
        c[(0, 0)].add(1)
        self.res = False
        if grid[0][0] == ")" or grid[-1][-1] == "(":
            return False
        dfs(0, 0, 1)
        # print(c)
        # dfs2(N - 1, M - 1, 1)
        return self.res
