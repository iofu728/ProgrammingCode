# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-09 11:14:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-09 11:15:01

"""
6919. 使数组中的所有元素都等于零 显示英文描述 
通过的用户数18
尝试过的用户数37
用户总通过次数18
用户总提交次数46
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。

你可以对数组执行下述操作 任意次 ：

从数组中选出长度为 k 的 任一 子数组，并将子数组中每个元素都 减去 1 。
如果你可以使数组中的所有元素都等于 0 ，返回  true ；否则，返回 false 。

子数组 是数组中的一个非空连续元素序列。

 

示例 1：

输入：nums = [2,2,3,1,1,0], k = 3
输出：true
解释：可以执行下述操作：
- 选出子数组 [2,2,3] ，执行操作后，数组变为 nums = [1,1,2,1,1,0] 。
- 选出子数组 [2,1,1] ，执行操作后，数组变为 nums = [1,1,1,0,0,0] 。
- 选出子数组 [1,1,1] ，执行操作后，数组变为 nums = [0,0,0,0,0,0] 。
示例 2：

输入：nums = [1,3,1,1], k = 2
输出：false
解释：无法使数组中的所有元素等于 0 。
 

提示：

1 <= k <= nums.length <= 105
0 <= nums[i] <= 106
"""
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        m = [nums[ii] - nums[ii - 1] if 0 < ii < N else (-nums[-1] if ii == N else nums[ii]) for ii in range(N + 1)]
        print(m)
        for ii in range(N + 1):
            if m[ii] < 0:
                return False
            # print(m, m[ii])
            if m[ii]:
                if ii + k > N:
                    return False
                m[ii + k] += m[ii]
            # print(m)
        return True

                