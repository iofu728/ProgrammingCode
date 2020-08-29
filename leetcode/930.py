# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-27 00:54:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-27 01:03:26


"""
930. Binary Subarrays With Sum Medium
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
Accepted 22,948 Submissions 52,949
"""


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        N, left, right, pre, sum_list, res = len(A), 0, 0, 0, [], 0
        sum_list.append(pre)
        for ii in A:
            pre += ii
            sum_list.append(pre)
        c = collections.Counter()
        for ii in sum_list:
            res += c[ii]
            c[ii + S] += 1
        return res
