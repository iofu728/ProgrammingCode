# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-01 17:34:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-01 17:35:07

"""
229. Majority Element II Medium
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
Accepted 145,050 Submissions 408,337
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        a1, a2 = -1, -1
        c1, c2 = 0, 0
        for ii in nums:
            if c1 == 0 and ii != a1 and ii != a2:
                a1 = ii
                c1 += 1
                continue
            elif c2 == 0 and ii != a1 and ii != a2:
                a2 = ii
                c2 += 1
                continue
            else:
                if a1 == ii:
                    c1 += 1
                elif a2 == ii:
                    c2 += 1
                else:
                    c1 -= 1
                    c2 -= 1
        print(a1, a2, c1, c2)
        cc1, cc2 = 0, 0
        for ii in nums:
            if c1 > 0 and ii == a1:
                cc1 += 1
            if c2 > 0 and ii == a2:
                cc2 += 1
        if cc1 > N // 3:
            res.append(a1)
        if cc2 > N // 3:
            res.append(a2)
        return res
