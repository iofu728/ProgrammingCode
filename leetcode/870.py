# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 16:33:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 16:34:06

"""
870. Advantage Shuffle Medium
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
Accepted 21,445 Submissions 46,920
"""


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        a = sorted(A)
        b = sorted(enumerate(B), key=lambda i: i[1])
        big = {ii: [] for ii in range(N)}
        small, jj = [], 0
        for ii in range(N):
            aa, (b_id, bb) = a[ii], b[jj]
            if aa > bb:
                big[b_id].append(aa)
                jj += 1
            else:
                small.append(aa)
        # print(big, small)
        return [big[ii].pop() if big[ii] else small.pop() for ii in range(N)]
