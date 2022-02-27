"""
1655. 分配重复整数
给你一个长度为 n 的整数数组 nums ，这个数组中至多有 50 个不同的值。同时你有 m 个顾客的订单 quantity ，其中，整数 quantity[i] 是第 i 位顾客订单的数目。请你判断是否能将 nums 中的整数分配给这些顾客，且满足：

第 i 位顾客 恰好 有 quantity[i] 个整数。
第 i 位顾客拿到的整数都是 相同的 。
每位顾客都满足上述两个要求。
如果你可以分配 nums 中的整数满足上面的要求，那么请返回 true ，否则返回 false 。

 

示例 1：

输入：nums = [1,2,3,4], quantity = [2]
输出：false
解释：第 0 位顾客没办法得到两个相同的整数。
示例 2：

输入：nums = [1,2,3,3], quantity = [2]
输出：true
解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
示例 3：

输入：nums = [1,1,2,2], quantity = [2,2]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
示例 4：

输入：nums = [1,1,2,3], quantity = [2,2]
输出：false
解释：尽管第 0 位顾客可以得到 [1,1] ，第 1 位顾客没法得到 2 个一样的整数。
示例 5：

输入：nums = [1,1,1,1,1], quantity = [2,3]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [1,1,1] 。
 

提示：

n == nums.length
1 <= n <= 105
1 <= nums[i] <= 1000
m == quantity.length
1 <= m <= 10
1 <= quantity[i] <= 105
nums 中至多有 50 个不同的数字。
通过次数2,412提交次数6,341
"""


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = list(Counter(nums).values())
        N, M = len(c), len(quantity)
        dp = [[False] * (1 << M) for ii in range(N + 1)]
        for ii in range(N + 1):
            dp[ii][0] = True
        cost = [0] * (1 << M)
        for ii in range(1 << M):
            tmp = 0
            for jj in range(M):
                if (ii >> jj) & 1:
                    tmp += quantity[jj]
            cost[ii] = tmp
        for ii in range(1, N + 1):
            dp[ii] = dp[ii - 1].copy()
            for jj in range(1 << M):
                tmp = jj
                while tmp:
                    if c[ii - 1] >= cost[tmp] and dp[ii - 1][jj ^ tmp]:
                        dp[ii][jj] = True
                        break
                    tmp = (tmp - 1) & jj
        return dp[-1][-1]
