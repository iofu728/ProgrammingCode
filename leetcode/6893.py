# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-25 10:18:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-25 10:18:59

"""
6893. 特别的排列 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Medium
给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。如果 nums 的一个排列满足以下条件，我们称它是一个特别的排列：

对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i] == 0 。
请你返回特别排列的总数目，由于答案可能很大，请将它对 109 + 7 取余 后返回。

 

示例 1：

输入：nums = [2,3,6]
输出：2
解释：[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。
示例 2：

输入：nums = [1,4,3]
输出：2
解释：[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。
 

提示：

2 <= nums.length <= 14
1 <= nums[i] <= 109
"""
MOD = 10 ** 9 + 7
class Solution:
    def specialPerm(self, nums: List[int]) -> int: 
        n = len(nums)  

        @lru_cache(None)  
        def dfs(mask, last_num):  
            if mask == (1 << n) - 1:  
                return 1  

            count = 0  
            for i, num in enumerate(nums):  
                if mask & (1 << i) == 0:  
                    if mask == 0 or last_num % num == 0 or num % last_num == 0:  
                        count += dfs(mask | (1 << i), num)  
                        count %= MOD  
            return count 

        return dfs(0, 1)
