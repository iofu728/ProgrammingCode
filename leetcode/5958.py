# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-12-19 11:17:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-12-19 11:17:42

"""
5958. 股票平滑下跌阶段的数目 显示英文描述 
User Accepted:6
User Tried:7
Total Accepted:6
Total Submissions:7
Difficulty:Medium
给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。

一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。

请你返回 平滑下降阶段 的数目。

 

示例 1：

输入：prices = [3,2,1,4]
输出：7
解释：总共有 7 个平滑下降阶段：
[3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1]
注意，仅一天按照定义也是平滑下降阶段。
示例 2：

输入：prices = [8,6,7,7]
输出：4
解释：总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7]
由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。
示例 3：

输入：prices = [1]
输出：1
解释：总共有 1 个平滑下降阶段：[1]
 

提示：

1 <= prices.length <= 105
1 <= prices[i] <= 105
"""
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N = len(prices)
        res = N
        dp = [prices[ii] - prices[ii - 1] for ii in range(1, N)]
        left = ([0] if N > 1 and dp[0] == -1 else []) + [ii for ii in range(1, N - 1) if dp[ii] == -1 and dp[ii - 1] != -1]
        right = [ii for ii in range(N - 2) if dp[ii] == -1 and dp[ii + 1] != -1] + ([N - 2] if N > 1 and dp[-1] == -1 else [])
        for ii, jj in zip(left, right):
            gap = jj - ii + 2
            res += (gap * (gap - 1) // 2)
        return res
            