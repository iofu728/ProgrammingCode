# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-02 11:37:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-02 11:38:16

"""
962. Maximum Width Ramp Medium
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

 

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
 

Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000
 
Accepted 20,731 Submissions 45,420
"""


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        res, pre = 0, float("inf")
        for ii in sorted(range(len(A)), key=lambda i: A[i]):
            res = max(res, ii - pre)
            pre = min(pre, ii)
        return res
