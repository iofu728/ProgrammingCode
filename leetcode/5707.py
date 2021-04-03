# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-04 01:16:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-04 01:17:13

"""
5707. 得到新鲜甜甜圈的最多组数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批顾客按数组中的顺序前来购买甜甜圈，其中 groups[i] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。

当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。

你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心。

 

示例 1：

输入：batchSize = 3, groups = [1,2,3,4,5,6]
输出：4
解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。
示例 2：

输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6]
输出：4
 

提示：

1 <= batchSize <= 9
1 <= groups.length <= 30
1 <= groups[i] <= 109
"""
from collections import defaultdict


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        N = batchSize
        gs = [c % N for c in groups]
        cs = [0] * N
        for c in gs:
            cs[c] += 1
        r = cs[0]
        dp = {}

        def dfs(s):
            k = 0
            for v in cs[1:]:
                k = (k << 5) + v
            if not k:
                return 0
            k = (k << 4) + s
            if k in dp:
                return dp[k]
            r = 0
            for i in range(1, N):
                if not cs[i]:
                    continue
                cs[i] -= 1
                t = dfs((s + i) % N)
                if not s:
                    t += 1
                if r < t:
                    r = t
                cs[i] += 1
            dp[k] = r
            return r

        return r + dfs(0)