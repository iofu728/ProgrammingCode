# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 09:21:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 09:22:11

"""
910. Smallest Range II Medium
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
Accepted 11,573 Submissions 43,371
"""
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        N = len(A)
        pre_min, pre_max = A[0], A[-1]
        ans = pre_max - pre_min
        for i in range(N - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(pre_max-K, a+K) - min(pre_min+K, b-K))
        return ans