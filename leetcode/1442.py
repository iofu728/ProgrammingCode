# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:04:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:08:47

"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR Medium
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
Example 3:

Input: arr = [2,3]
Output: 0
Example 4:

Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
Accepted 13,281 Submissions 18,955
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        A, pre = [arr[0]], arr[0]
        for ii in arr[1:]:
            pre ^= ii
            A.append(pre)
        res = 0
        for ii in range(N):
            for kk in range(ii + 1, N):
                a_i, a_k = A[ii - 1] if ii else 0, A[kk]
                a_ik = a_k ^ a_i
                if not a_ik:
                    res += kk - ii
        return res

