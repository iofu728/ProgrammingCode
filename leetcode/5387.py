# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-02 23:02:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-03 00:08:38

"""
5387. 每个人戴不同帽子的方案数 显示英文描述 
通过的用户数9
尝试过的用户数31
用户总通过次数9
用户总提交次数39
题目难度Hard
总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。

给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表。

请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。

由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。

示例 1：

输入：hats = [[3,4],[4,5],[5]]
输出：1
解释：给定条件下只有一种方法选择帽子。
第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。
示例 2：

输入：hats = [[3,5,1],[3,5]]
输出：4
解释：总共有 4 种安排帽子的方法：
(3,5)，(5,3)，(1,3) 和 (1,5)
示例 3：

输入：hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
输出：24
解释：每个人都可以从编号为 1 到 4 的帽子中选。
(1,2,3,4) 4 个帽子的排列方案数为 24 。
示例 4：

输入：hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
输出：111

提示：

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] 包含一个数字互不相同的整数列表。
"""
from functools import reduce


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        hats = sorted(hats, key=lambda i: len(i))

        def bfs(a):
            if len(a) == 1:
                return len(a[0])
            len_a = [len(ii) for ii in a]
            if 0 in len_a:
                return 0
            len_list = [jj for ii in a for jj in ii]
            if len(set(len_list)) == len(len_list):
                return reduce(lambda x, y: x * y, len_a)
            res = []
            for t in a[0]:
                tmp = a[1:][:]
                tmp = [[jj for jj in ii if jj != t] for ii in tmp]
                res.append(bfs(tmp))
            return sum(res)

        return bfs(hats)


class Solution:
    MOD = 10 ** 9 + 7

    def numberWays(self, hats):
        N = len(hats)
        pn = 2 ** N
        dp = [[None for j in range(pn)] for i in range(0, 41)]
        back = [[] for i in range(0, 41)]
        for i in range(N):
            for hat in hats[i]:
                back[hat].append(i)
        dp[0][0] = 1
        for i in range(1, 41):
            for j in range(pn):
                dp[i][j] = dp[i - 1][j]
                for k in back[i]:
                    pk = 1 << k
                    if pk & j == 0:
                        continue
                    if dp[i - 1][j - pk] is None:
                        continue
                    if dp[i][j] is None:
                        dp[i][j] = 0
                    dp[i][j] += dp[i - 1][j - pk]
                    dp[i][j] %= self.MOD
        if dp[-1][-1] is None:
            return 0
        else:
            return dp[-1][-1]
