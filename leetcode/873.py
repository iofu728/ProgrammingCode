# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-23 22:47:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-23 22:50:42

"""
873. Length of Longest Fibonacci Subsequence
Medium

831

35

Add to List

Share
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
 

Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)
Accepted 33,229 Submissions 69,292
"""
import heapq
import bisect


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        dp = defaultdict(int)
        nums = set(A)
        for jj in range(N):
            for ii in range(jj):
                if A[jj] - A[ii] < A[ii] and A[jj] - A[ii] in nums:
                    dp[(A[ii], A[jj])] = dp.get((A[jj] - A[ii], A[ii]), 2) + 1
        return max(dp.values() or [0])

