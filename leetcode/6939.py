# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-13 11:20:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-13 11:21:06

"""
6939. 数组中的最大数对和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个下标从 0 开始的整数数组 nums 。请你从 nums 中找出和 最大 的一对数，且这两个数数位上最大的数字相等。

返回最大和，如果不存在满足题意的数字对，返回 -1 。

 

示例 1：

输入：nums = [51,71,17,24,42]
输出：88
解释：
i = 1 和 j = 2 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 71 + 17 = 88 。 
i = 3 和 j = 4 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 24 + 42 = 66 。
可以证明不存在其他数对满足数位上最大的数字相等，所以答案是 88 。
示例 2：

输入：nums = [1,2,3,4]
输出：-1
解释：不存在数对满足数位上最大的数字相等。
 

提示：

2 <= nums.length <= 100
1 <= nums[i] <= 104
"""
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        c = defaultdict(list)
        for ii in nums:
            y = max(str(ii))
            c[y].append(ii)
        res = -1
        for k, v in c.items():
            if len(v) >= 2:
                res = max(res, sum(sorted(v)[-2:]))
        return res
            