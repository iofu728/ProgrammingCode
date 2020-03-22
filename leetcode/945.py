# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 18:08:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 19:09:44

"""
945. Minimum Increment to Make Array Unique Medium

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

## Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

## Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 
## Note:
0 <= A.length <= 40000
0 <= A[i] < 40000
 
Accepted 20,801 Submissions 45,810
"""


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A = sorted(A)
        A.append(100000)
        taken = ans = 0
        for ii in range(1, len(A)):
            if A[ii - 1] == A[ii]:
                taken += 1
                ans -= A[ii]
            else:
                m = min(taken, A[ii] - A[ii - 1] - 1)
                ans += m * (m + 1 + 2 * A[ii - 1]) // 2
                taken -= m
        return ans
