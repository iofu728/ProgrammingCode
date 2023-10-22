# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-12 22:56:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-12 22:56:46

"""
2874. 有序三元组中的最大值 II 显示英文描述 
通过的用户数1434
尝试过的用户数1944
用户总通过次数1478
用户总提交次数4419
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 。

请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。

下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。

 

示例 1：

输入：nums = [12,6,1,2,7]
输出：77
解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。
可以证明不存在值大于 77 的有序下标三元组。
示例 2：

输入：nums = [1,10,3,4,19]
输出：133
解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。
可以证明不存在值大于 133 的有序下标三元组。 
示例 3：

输入：nums = [1,2,3]
输出：0
解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。
 

提示：

3 <= nums.length <= 105
1 <= nums[i] <= 106
"""
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        m, n = [0] * N, [0] * N
        pre = 0 
        for ii in range(N - 1, -1, -1):
            pre = max(pre, nums[ii])
            m[ii] = pre
        pre = 0 
        for ii in range(N):
            pre = max(pre, nums[ii])
            n[ii] = pre
        res = 0
        for jj in range(1, N - 1):
            tmp = (n[jj - 1] - nums[jj]) * m[jj + 1]
            res = max(tmp, res)
        return res