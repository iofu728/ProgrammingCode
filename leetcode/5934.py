# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-12-12 00:22:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-12-12 00:22:47

"""
5934. 找到和最大的长度为 K 的子序列 显示英文描述 
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
给你一个整数数组 nums 和一个整数 k 。你需要找到 nums 中长度为 k 的 子序列 ，且这个子序列的 和最大 。

请你返回 任意 一个长度为 k 的整数子序列。

子序列 定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。

 

示例 1：

输入：nums = [2,1,3,3], k = 2
输出：[3,3]
解释：
子序列有最大和：3 + 3 = 6 。
示例 2：

输入：nums = [-1,-2,3,4], k = 3
输出：[-1,3,4]
解释：
子序列有最大和：-1 + 3 + 4 = 6 。
示例 3：

输入：nums = [3,4,3,3], k = 2
输出：[3,4]
解释：
子序列有最大和：3 + 4 = 7 。
另一个可行的子序列为 [4, 3] 。
 

提示：

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
"""

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        k = sorted(enumerate(nums), key=lambda x:x[1])[-1 * k:]
        return [jj for ii, jj in sorted(k, key=lambda x:x[0])]