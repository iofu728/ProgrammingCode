# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 23:17:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 23:18:51

"""
786. K-th Smallest Prime Fraction Hard
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.
Accepted 14,305 Submissions 34,905
"""
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        N = len(A)
        dp = [N - 1] * N
        res = 0
        heap = [(A[ii] / A[-1], ii) for ii in range(N - 1)]
        heapq.heapify(heap)
        while heap:
            _, row = heapq.heappop(heap)
            # print(row, dp[row], heap, res)
            res += 1
            if res == K:
                return [A[row], A[dp[row]]]
            if dp[row] > row + 1:
                dp[row] -= 1
                if dp[row] == row and row:
                    dp[now] -= 1
                heapq.heappush(heap, (A[row] / A[dp[row]], row))
        return []

