# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-30 23:38:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-30 23:39:51

"""
84. Largest Rectangle in Histogram Hard
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
Accepted 268,048 Submissions 765,469
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        left, right = [0] * N, [0] * N

        stack1, stack2 = [], []
        for ii in range(N):
            while stack1 and heights[stack1[-1]] >= heights[ii]:
                stack1.pop()
            left[ii] = stack1[-1] if stack1 else -1
            stack1.append(ii)
        for ii in range(N - 1, -1, -1):
            while stack2 and heights[stack2[-1]] >= heights[ii]:
                stack2.pop()
            right[ii] = stack2[-1] if stack2 else N
            stack2.append(ii)
        ans = (
            max([(jj - ii - 1) * kk for ii, jj, kk in zip(left, right, heights)])
            if N
            else 0
        )
        return ans
