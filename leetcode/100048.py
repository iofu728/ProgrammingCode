# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-24 12:47:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-24 12:47:41

"""
100048. 美丽塔 II 显示英文描述 
通过的用户数3
尝试过的用户数5
用户总通过次数3
用户总提交次数8
题目难度Medium
给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。

你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。

如果以下条件满足，我们称这些塔是 美丽 的：

1 <= heights[i] <= maxHeights[i]
heights 是一个 山状 数组。
如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山状 数组：

对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
请你返回满足 美丽塔 要求的方案中，高度和的最大值 。

 

示例 1：

输入：maxHeights = [5,3,4,1,1]
输出：13
解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]  
- heights 是个山状数组，峰值在 i = 0 处。
13 是所有美丽塔方案中的最大高度和。
示例 2：

输入：maxHeights = [6,5,3,9,2,7]
输出：22
解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山状数组，峰值在 i = 3 处。
22 是所有美丽塔方案中的最大高度和。
示例 3：

输入：maxHeights = [3,2,5,5,2,3]
输出：18
解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山状数组，最大值在 i = 2 处。
注意，在这个方案中，i = 3 也是一个峰值。
18 是所有美丽塔方案中的最大高度和。
 

提示：

1 <= n == maxHeights <= 105
1 <= maxHeights[i] <= 109

"""
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        @lru_cache(None)
        def dfs_l(idx):
            if idx == -1:
                return 0
            return maxHeights[idx] * (idx - ll[idx]) + dfs_l(ll[idx])
            
            
        @lru_cache(None)
        def dfs_r(idx):
            if idx == N:
                return 0
            return maxHeights[idx] * (rr[idx] - idx) + dfs_r(rr[idx])
        N = len(maxHeights)
        ll = [-1] * N
        rr = [N] * N
        q = []
        for ii, jj in enumerate(maxHeights):
            while q and q[-1][0] >= jj:
                q.pop()
            q.append((jj, ii))
            if len(q) > 1:
                ll[ii] = q[-2][1]
        q = []
        for ii in range(N - 1, -1, -1):
            jj = maxHeights[ii]
            while q and q[-1][0] >= jj:
                q.pop()
            q.append((jj, ii))
            if len(q) > 1:
                rr[ii] = q[-2][1]
        # print(ll, rr)
        res = 0
        for ii in range(N):
            # print(dfs_l(ii), dfs_r(ii))
            res = max(res, dfs_l(ii) + dfs_r(ii) - maxHeights[ii])
        return res
        