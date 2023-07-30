# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-30 12:37:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-30 12:37:42

"""
6900. 统计完全子数组的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个由 正 整数组成的数组 nums 。

如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：

子数组中 不同 元素的数目等于整个数组不同元素的数目。
返回数组中 完全子数组 的数目。

子数组 是数组中的一个连续非空序列。

 

示例 1：

输入：nums = [1,3,1,2,2]
输出：4
解释：完全子数组有：[1,3,1,2]、[1,3,1,2,2]、[3,1,2] 和 [3,1,2,2] 。
示例 2：

输入：nums = [5,5,5,5]
输出：10
解释：数组仅由整数 5 组成，所以任意子数组都满足完全子数组的条件。子数组的总数为 10 。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2000
"""
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c = Counter(nums)
        l, r = 0, 0
        N = len(nums)
        res = 0
        l = 0
        r = l
        tmp = Counter([nums[r]])
        while r + 1 < N:
            if len(tmp) == len(c):
                break
            r += 1
            tmp[nums[r]] += 1
        if len(tmp) == len(c):
            # print(l, r, N - r)
            res += (N - r)
        for l in range(1, N):
            tmp[nums[l - 1]] -= 1
            if tmp[nums[l - 1]] == 0:
                del tmp[nums[l - 1]]
            while r + 1 < N:
                if len(tmp) == len(c):
                    break
                r += 1
                tmp[nums[r]] += 1
            if len(tmp) == len(c):
                # print(l, r, N - r)
                res += (N - r)
            
            
        return res
            