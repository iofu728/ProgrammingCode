"""
100534. 最多 K 个元素的子序列的最值之和 显示英文描述 
通过的用户数0
尝试过的用户数8
用户总通过次数0
用户总提交次数8
题目难度Medium
给你一个整数数组 nums 和一个正整数 k，返回所有长度最多为 k 的 子序列 中 最大值 与 最小值 之和的总和。

非空子序列 是指从另一个数组中删除一些或不删除任何元素（且不改变剩余元素的顺序）得到的数组。

由于答案可能非常大，请返回对 109 + 7 取余数的结果。

 

示例 1：

输入： nums = [1,2,3], k = 2

输出： 24

解释：

数组 nums 中所有长度最多为 2 的子序列如下：

子序列	最小值	最大值	和
[1]	1	1	2
[2]	2	2	4
[3]	3	3	6
[1, 2]	1	2	3
[1, 3]	1	3	4
[2, 3]	2	3	5
总和	 	 	24
因此，输出为 24。

示例 2：

输入： nums = [5,0,6], k = 1

输出： 22

解释：

对于长度恰好为 1 的子序列，最小值和最大值均为元素本身。因此，总和为 5 + 5 + 0 + 0 + 6 + 6 = 22。

示例 3：

输入： nums = [1,1,1], k = 2

输出： 12

解释：

子序列 [1, 1] 和 [1] 各出现 3 次。对于所有这些子序列，最小值和最大值均为 1。因此，总和为 12。

 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= min(100, nums.length)
"""
class Solution:
    MODS = 10**9 + 7
    def minMaxSums(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums = sorted(nums)
        dp = [1] * (N + 1)
        for ii in range(1, N + 1):
            dp[ii] = (dp[ii - 1] * 2) % self.MODS
        inv = [1] * (k + 1)
        for ii in range(2, k + 1):
            inv[ii] = pow(ii, self.MODS - 2, self.MODS)
        s = [0] * (N + 1)
        for ii in range(N + 1):
            if ii < k:
                s[ii] = dp[ii]
            else:
                c, tmp = 1, 1
                for jj in range(1, k):
                    c = c * (ii - jj + 1) % self.MODS
                    c = c * inv[jj] % self.MODS
                    tmp = (tmp + c) % self.MODS
                s[ii] = tmp
        res = 0
        for ii in range(N):
            now = (s[ii] + s[N - 1 - ii]) % self.MODS
            res = (res + now * nums[ii]) % self.MODS
        return res
