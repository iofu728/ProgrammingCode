# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-30 11:53:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-30 11:53:25

"""
100357. 找出有效子序列的最大长度 I 显示英文描述 
通过的用户数9
尝试过的用户数12
用户总通过次数9
用户总提交次数12
题目难度Medium
给你一个整数数组 nums。

nums 的子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列：

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2
返回 nums 的 最长的有效子序列 的长度。

一个 子序列 指的是从原数组中删除一些元素（也可以不删除任何元素），剩余元素保持原来顺序组成的新数组。

 

示例 1：

输入： nums = [1,2,3,4]

输出： 4

解释：

最长的有效子序列是 [1, 2, 3, 4]。

示例 2：

输入： nums = [1,2,1,1,2,1,2]

输出： 6

解释：

最长的有效子序列是 [1, 2, 1, 2, 1, 2]。

示例 3：

输入： nums = [1,3]

输出： 2

解释：

最长的有效子序列是 [1, 3]。

 

提示：

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107

"""
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [ii % 2 for ii in nums]
        N = len(nums)
        c = Counter(nums)
        res = max(c.values())
        c = Counter([])
        a, b = 0, 0
        ai, bi = 0, 0
        for ii in nums:
            if ai % 2 == 0 or bi % 2 == 1:
                if ii == 0:
                    if ai % 2 == 0:
                        a += 1
                        ai += 1
                    if bi % 2 == 1:
                        b += 1
                        bi += 1
            if ai % 2 == 1 or bi % 2 == 0:
                if ii == 1:    
                    if ai % 2 == 1:
                        a += 1
                        ai += 1
                    if bi % 2 == 0:
                        b += 1
                        bi += 1
        return max(res, ai, bi)
                        
            