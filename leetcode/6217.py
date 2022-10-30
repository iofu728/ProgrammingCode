# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-23 11:25:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-23 11:25:44

"""
6217. 使数组相似的最少操作次数 显示英文描述 
通过的用户数184
尝试过的用户数211
用户总通过次数190
用户总提交次数252
题目难度Hard
给你两个正整数数组 nums 和 target ，两个数组长度相等。

在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：

令 nums[i] = nums[i] + 2 且
令 nums[j] = nums[j] - 2 。
如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。

请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。

 

示例 1：

输入：nums = [8,12,6], target = [2,14,10]
输出：2
解释：可以用两步操作将 nums 变得与 target 相似：
- 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。
- 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。
2 次操作是最少需要的操作次数。
示例 2：

输入：nums = [1,2,5], target = [4,1,3]
输出：1
解释：一步操作可以使 nums 变得与 target 相似：
- 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。
示例 3：

输入：nums = [1,1,1,1,1], target = [1,1,1,1,1]
输出：0
解释：数组 nums 已经与 target 相似。
 

提示：

n == nums.length == target.length
1 <= n <= 105
1 <= nums[i], target[i] <= 106
nums 一定可以变得与 target 相似。
"""
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        a1, a2 = sorted([ii for ii in nums if ii % 2 == 0]), sorted([ii for ii in target if ii % 2 == 0])
        b1, b2 = sorted([ii for ii in nums if ii % 2 == 1]), sorted([ii for ii in target if ii % 2 == 1])
        # print(a1, a2)
        # print(b1, b2)
        x, y = 0, 0
        for ii, jj in zip(a1, a2):
            if ii > jj:
                x += (ii - jj) // 2
            else:
                y += (jj - ii) // 2
        for ii, jj in zip(b1, b2):
            if ii > jj:
                x += (ii - jj) // 2
            else:
                y += (jj - ii) // 2
        return max(x, y)
        