# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-04 10:55:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-04 11:20:40

"""
42. Trapping Rain Water Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

## Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Accepted 451,335 Submissions 956,232
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left, right, pre, before, ans = [0] * N, [0] * N, 0, 0, 0
        for idx, ii in enumerate(height):
            pre = max(ii, pre)
            left[idx] = pre
        for idx in range(N - 1, -1, -1):
            before = max(before, height[idx])
            right[idx] = before
            ans += min(before, left[idx]) - height[idx]
        return ans
