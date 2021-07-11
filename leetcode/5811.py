"""
5811. 用三种不同颜色为网格涂色 显示英文描述 
通过的用户数6
尝试过的用户数6
用户总通过次数6
用户总提交次数6
题目难度Hard
给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。

涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。

 

示例 1：


输入：m = 1, n = 1
输出：3
解释：如上图所示，存在三种可能的涂色方案。
示例 2：


输入：m = 1, n = 2
输出：6
解释：如上图所示，存在六种可能的涂色方案。
示例 3：

输入：m = 5, n = 5
输出：580986
 

提示：

1 <= m <= 5
1 <= n <= 1000
"""


class Solution:
    MOD = 10 ** 9 + 7

    def colorTheGrid(self, m: int, n: int) -> int:
        base, wait = [], [0, 1, 2]

        def dfs(now):
            if len(now) == m:
                base.append(now)
                return
            for ii in wait:
                if not now or ii != now[-1]:
                    dfs(now + [ii])

        dfs([])
        N = len(base)
        dp = [[0] * N for _ in range(n)]
        dp[0] = [1] * N
        can = defaultdict(list)
        for ii in range(N):
            for jj in range(N):
                flag = True
                for kk in range(m):
                    if base[ii][kk] == base[jj][kk]:
                        flag = False
                        break
                if flag:
                    can[ii].append(jj)

        for ii in range(1, n):
            for jj in range(N):
                for kk in can[jj]:
                    dp[ii][jj] += dp[ii - 1][kk]
                    dp[ii][jj] %= self.MOD
        return sum(dp[-1]) % self.MOD
