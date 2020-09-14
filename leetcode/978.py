# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 20:42:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 20:42:56

"""
978. Longest Turbulent Subarray Medium
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
 

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
Accepted 31,029 Submissions 66,607
"""
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        bulen = [
            1 if (A[ii] < A[ii + 1]) else (2 if (A[ii] > A[ii + 1]) else 0)
            for ii in range(N - 1)
        ]
        # print(bulen)
        tmp, res, pre = 0, 0, 0
        for ii in bulen:
            # print(tmp, res, pre)
            if ii == 0 or ii == pre:
                res = max(res, tmp)
                tmp = 0 if ii == 0 else 1
                pre = ii
            else:
                tmp += 1
                pre = ii
        return max(res, tmp) + 1
