# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-10 23:57:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-10 23:58:04

"""
354. Russian Doll Envelopes Hard
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Accepted 60,052 Submissions 171,595
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda i: (i[0], -i[-1]))
        # print(envelopes)
        N = len(envelopes)
        dp = [1] * N
        for ii in range(N):
            tt = [dp[jj] for jj in range(ii) if envelopes[ii][1] > envelopes[jj][1]]
            if len(tt):
                dp[ii] = max(tt) + 1
        # print(dp)
        return max(dp) if N else 0
