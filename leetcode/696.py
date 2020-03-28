# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 20:56:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 21:14:47

"""
696. Count Binary Substrings Easy
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

## Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

## Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

## Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
Accepted 41,305 Submissions 74,831
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        if N < 2:
            return 0
        result = []
        change = [ii for ii in range(1, N) if s[ii] != s[ii - 1]]
        for e in change:
            b = e - 1
            t = s[b]
            while b >= 0 and e < N:
                if s[b] == t and s[e] != t:
                    result.append(s[b : e + 1])
                else:
                    break
                b, e = b - 1, e + 1
        # print(result)
        return len(result)
