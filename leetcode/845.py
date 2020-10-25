# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-25 16:06:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-25 16:08:01

"""
845. Longest Mountain in Array Medium
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
Accepted 39,546 Submissions 104,948
"""


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        b = [
            (ii, 0)
            for ii in range(N - 2)
            if (ii == 0 and A[ii] < A[ii + 1])
            or (ii and A[ii - 1] >= A[ii] and A[ii] < A[ii + 1])
        ]
        e = [
            (ii, 2)
            for ii in range(2, N)
            if (ii == N - 1 and A[ii] < A[ii - 1])
            or (ii != N - 1 and A[ii + 1] >= A[ii] and A[ii] < A[ii - 1])
        ]
        same = [(ii, 1) for ii in range(N - 1) if A[ii] == A[ii + 1]]
        ss = sorted(b + e + same, key=lambda i: (i[0], -i[1]))
        res = 0
        # print(ss)
        while ss:
            t1 = ss.pop(0)
            while ss and (t1[1] != 0 or ss[0][1] == 0):
                t1 = ss.pop(0)
            if not ss or ss[0][1] != 2:
                continue
            t2 = ss.pop(0)
            res = max(t2[0] - t1[0] + 1, res)
        return res
