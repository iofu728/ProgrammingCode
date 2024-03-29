# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-03-26 13:17:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-03-26 13:17:15

"""
6355. 质数减法运算 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个下标从 0 开始的整数数组 nums ，数组长度为 n 。

你可以执行无限次下述运算：

选择一个之前未选过的下标 i ，并选择一个 严格小于 nums[i] 的质数 p ，从 nums[i] 中减去 p 。
如果你能通过上述运算使得 nums 成为严格递增数组，则返回 true ；否则返回 false 。

严格递增数组 中的每个元素都严格大于其前面的元素。

 

示例 1：

输入：nums = [4,9,6,10]
输出：true
解释：
在第一次运算中：选择 i = 0 和 p = 3 ，然后从 nums[0] 减去 3 ，nums 变为 [1,9,6,10] 。
在第二次运算中：选择 i = 1 和 p = 7 ，然后从 nums[1] 减去 7 ，nums 变为 [1,2,6,10] 。
第二次运算后，nums 按严格递增顺序排序，因此答案为 true 。
示例 2：

输入：nums = [6,8,11,12]
输出：true
解释：nums 从一开始就按严格递增顺序排序，因此不需要执行任何运算。
示例 3：

输入：nums = [5,8,3]
输出：false
解释：可以证明，执行运算无法使 nums 按严格递增顺序排序，因此答案是 false 。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
"""


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        X = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
            101,
            103,
            107,
            109,
            113,
            127,
            131,
            137,
            139,
            149,
            151,
            157,
            163,
            167,
            173,
            179,
            181,
            191,
            193,
            197,
            199,
            211,
            223,
            227,
            229,
            233,
            239,
            241,
            251,
            257,
            263,
            269,
            271,
            277,
            281,
            283,
            293,
            307,
            311,
            313,
            317,
            331,
            337,
            347,
            349,
            353,
            359,
            367,
            373,
            379,
            383,
            389,
            397,
            401,
            409,
            419,
            421,
            431,
            433,
            439,
            443,
            449,
            457,
            461,
            463,
            467,
            479,
            487,
            491,
            499,
            503,
            509,
            521,
            523,
            541,
            547,
            557,
            563,
            569,
            571,
            577,
            587,
            593,
            599,
            601,
            607,
            613,
            617,
            619,
            631,
            641,
            643,
            647,
            653,
            659,
            661,
            673,
            677,
            683,
            691,
            701,
            709,
            719,
            727,
            733,
            739,
            743,
            751,
            757,
            761,
            769,
            773,
            787,
            797,
            809,
            811,
            821,
            823,
            827,
            829,
            839,
            853,
            857,
            859,
            863,
            877,
            881,
            883,
            887,
            907,
            911,
            919,
            929,
            937,
            941,
            947,
            953,
            967,
            971,
            977,
            983,
            991,
            997,
            1009,
        ]
        N = len(nums)
        idx = N - 2
        pre = nums[-1]
        while idx >= 0:
            now = nums[idx]
            if now >= pre:
                gap = now - pre + 1
                i = bisect.bisect_left(X, gap)
                if X[i] >= now:
                    return False
                now -= X[i]
            # print(idx, now)
            idx -= 1
            pre = now

        return True
