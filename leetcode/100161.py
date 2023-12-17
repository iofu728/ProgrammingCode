# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-12-17 12:13:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-12-17 12:13:20

"""
100161. 划分数组并满足最大差限制 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个长度为 n 的整数数组 nums，以及一个正整数 k 。

将这个数组划分为一个或多个长度为 3 的子数组，并满足以下条件：

nums 中的 每个 元素都必须 恰好 存在于某个子数组中。
子数组中 任意 两个元素的差必须小于或等于 k 。
返回一个 二维数组 ，包含所有的子数组。如果不可能满足条件，就返回一个空数组。如果有多个答案，返回 任意一个 即可。

 

示例 1：

输入：nums = [1,3,4,8,7,9,3,5,1], k = 2
输出：[[1,1,3],[3,4,5],[7,8,9]]
解释：可以将数组划分为以下子数组：[1,1,3]，[3,4,5] 和 [7,8,9] 。
每个子数组中任意两个元素的差都小于或等于 2 。
注意，元素的顺序并不重要。
示例 2：

输入：nums = [1,3,3,2,7,3], k = 3
输出：[]
解释：无法划分数组满足所有条件。
 

提示：

n == nums.length
1 <= n <= 105
n 是 3 的倍数
1 <= nums[i] <= 105
1 <= k <= 105
"""
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        for ii in range(0, n, 3):
            if nums[ii + 2] - nums[ii] > k:
                return []
        return [[nums[ii], nums[ii + 1], nums[ii + 2]] for ii in range(0, n, 3)]