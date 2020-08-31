# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 17:23:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 17:24:30

"""
1014. Best Sightseeing Pair Medium
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

Note:

2 <= A.length <= 50000
1 <= A[i] <= 1000
Accepted 18,034 Submissions 34,284
"""
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        N = len(A)
        mx, ans = A[0] + 0, 0
        for ii in range(1, N):
            ans = max(ans, mx + A[ii] - ii)
            mx = max(mx, A[ii] + ii)
        return ans
