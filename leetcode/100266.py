"""
100266. 交替子数组计数 显示英文描述 
通过的用户数4
尝试过的用户数5
用户总通过次数4
用户总提交次数5
题目难度Medium
给你一个二进制数组 nums 。

如果一个子数组中 不存在 两个 相邻 元素的值 相同 的情况，我们称这样的子数组为 交替子数组 。

返回数组 nums 中交替子数组的数量。

 

示例 1：

输入： nums = [0,1,1,1]

输出： 5

解释：

以下子数组是交替子数组：[0] 、[1] 、[1] 、[1] 以及 [0,1] 。

示例 2：

输入： nums = [1,0,1,0]

输出： 10

解释：

数组的每个子数组都是交替子数组。可以统计在内的子数组共有 10 个。

 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1 。
"""
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # s = 0
        # c = defaultdict(int)
        # N = len(nums)
        # dp = [0] * N
        # for ii in range(N):
        #     dp[ii] = s - c[nums[ii]] + 1
        #     s += dp[ii]
        #     c[nums[ii]] += dp[ii]
        # print(dp)
        # return sum(dp)
        def get_c(a):
            return a * (a + 1) // 2
        c = 1
        N = len(nums)
        res = 0
        for ii in range(1, N):
            if nums[ii - 1] == nums[ii]:
                res += get_c(c)
                # print(c, get_c(c))
                c = 1
            else:
                c += 1
        res += get_c(c)
        return res
                