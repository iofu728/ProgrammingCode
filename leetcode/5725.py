# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-04 12:36:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-04 12:36:32
"""
5725. 序列中不同最大公约数的数目 显示英文描述 
通过的用户数103
尝试过的用户数903
用户总通过次数133
用户总提交次数2278
题目难度Hard
给你一个由正整数组成的数组 nums 。

数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。

例如，序列 [4,6,16] 的最大公约数是 2 。
数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。

 

示例 1：


输入：nums = [6,10,3]
输出：5
解释：上图显示了所有的非空子序列与各自的最大公约数。
不同的最大公约数为 6 、10 、3 、2 和 1 。
示例 2：

输入：nums = [5,15,40,5,6]
输出：7
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 105
"""

from functools import lru_cache


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        from math import gcd

        tag = [False for i in range(max(nums) + 1)]
        for n in nums:
            tag[n] = True

        ans = 0
        for i in range(1, len(tag)):
            cur_gcd = -1
            for j in range(i, len(tag), i):
                if tag[j]:
                    cur_gcd = gcd(cur_gcd, j) if cur_gcd != -1 else j
                    if cur_gcd == i:
                        ans += 1
                        break
        return ans