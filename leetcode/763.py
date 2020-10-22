# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-22 01:29:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-22 01:29:43

"""
763. Partition Labels Medium
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
 

Accepted 190,599 Submissions 246,021
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        start, end = {}, {}
        for ii, jj in enumerate(S):
            if jj not in start:
                start[jj] = ii
            end[jj] = ii
        res, pre, e, idx = [], 0, end[S[0]], 0
        while idx < len(S):
            e = end[S[idx]]
            while idx < e:
                e = max(e, end[S[idx]])
                idx += 1
            res.append(e - pre + 1)
            pre = e + 1
            idx += 1
        return res