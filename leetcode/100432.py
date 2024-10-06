# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-10-07 00:15:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-10-07 00:15:41

"""
100432. 连接二进制表示可形成的最大数值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个长度为 3 的整数数组 nums。

现以某种顺序 连接 数组 nums 中所有元素的 二进制表示 ，请你返回可以由这种方法形成的 最大 数值。

注意 任何数字的二进制表示 不含 前导零。

 

示例 1:

输入: nums = [1,2,3]

输出: 30

解释:

按照顺序 [3, 1, 2] 连接数字的二进制表示，得到结果 "11110"，这是 30 的二进制表示。

示例 2:

输入: nums = [2,8,16]

输出: 1296

解释:

按照顺序 [2, 8, 16] 连接数字的二进制表述，得到结果 "10100010000"，这是 1296 的二进制表示。

 

提示:

nums.length == 3
1 <= nums[i] <= 127
"""
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        max_value = 0
        for perm in permutations(nums):
            binary_strings = [bin(num)[2:] for num in perm]
            concatenated_binary = ''.join(binary_strings)
            decimal_value = int(concatenated_binary, 2)
            max_value = max(max_value, decimal_value)
        return max_value