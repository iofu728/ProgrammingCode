# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-05 15:59:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-05 15:59:56

"""
1671. 得到山形数组的最少删除次数
我们定义 arr 是 山形数组 当且仅当它满足：

arr.length >= 3
存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。

 

示例 1：

输入：nums = [1,3,1]
输出：0
解释：数组本身就是山形数组，所以我们不需要删除任何元素。
示例 2：

输入：nums = [2,1,1,5,6,2,3,1]
输出：3
解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
示例 3：

输入：nums = [4,3,2,1,1,2,3,1]
输出：4
提示：

输入：nums = [1,2,3,4,4,3,2,1]
输出：1
 

提示：

3 <= nums.length <= 1000
1 <= nums[i] <= 109
题目保证 nums 删除一些元素后一定能得到山形数组。
通过次数2,338提交次数5,009
"""


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def LIS(nums):
            dp = [1] * N
            s = [nums[0]]
            for ii in range(1, N):
                idx = bisect.bisect_left(s, nums[ii])
                if idx == len(s):
                    s.append(nums[ii])
                else:
                    s[idx] = nums[ii]
                dp[ii] = idx + 1
            return dp

        N = len(nums)
        l, r = LIS(nums), LIS(nums[::-1])[::-1]
        # print(l, r)
        res = 0
        for ii in range(N):
            if l[ii] > 1 and r[ii] > 1:
                res = max(res, l[ii] + r[ii] - 1)
        return N - res
