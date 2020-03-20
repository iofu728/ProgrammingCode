# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-20 14:33:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-20 14:33:44

"""
907. Sum of Subarray Minimums
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
 

通过次数3,377提交次数12,070
"""


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        ans = dot = 0
        for j, k in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= k:
                m, n = stack.pop()
                dot -= m * n
                count += n
            stack.append((k, count))
            dot += k * count  # min Stack [i, j] + now dot
            ans += dot
        return ans
