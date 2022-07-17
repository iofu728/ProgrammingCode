# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-17 11:23:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-17 11:24:00

"""
6122. 使数组可以被整除的最少删除次数 显示英文描述 
通过的用户数38
尝试过的用户数43
用户总通过次数38
用户总提交次数50
题目难度Hard
给你两个正整数数组 nums 和 numsDivide 。你可以从 nums 中删除任意数目的元素。

请你返回使 nums 中 最小 元素可以整除 numsDivide 中所有元素的 最少 删除次数。如果无法得到这样的元素，返回 -1 。

如果 y % x == 0 ，那么我们说整数 x 整除 y 。

 

示例 1：

输入：nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
输出：2
解释：
[2,3,2,4,3] 中最小元素是 2 ，它无法整除 numsDivide 中所有元素。
我们从 nums 中删除 2 个大小为 2 的元素，得到 nums = [3,4,3] 。
[3,4,3] 中最小元素为 3 ，它可以整除 numsDivide 中所有元素。
可以证明 2 是最少删除次数。
示例 2：

输入：nums = [4,3,6], numsDivide = [8,2,6,10]
输出：-1
解释：
我们想 nums 中的最小元素可以整除 numsDivide 中的所有元素。
没有任何办法可以达到这一目的。
 

提示：

1 <= nums.length, numsDivide.length <= 105
1 <= nums[i], numsDivide[i] <= 109
"""
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        @lru_cache(None)
        def gcd(x, y):
            return math.gcd(x, y)
        N, M = len(nums), len(numsDivide)
        k = gcd(numsDivide[0], numsDivide[1]) if M >= 2 else numsDivide[0]
        for ii in numsDivide[2:]:
            k = gcd(k, ii)
            if k == 1:
                break
        c = Counter(nums)
        tmp = 0
        for ii in sorted(c.keys()):
            if k % ii == 0:
                return tmp
            tmp += c[ii]
            if ii >= k:
                break
        return -1
                
        