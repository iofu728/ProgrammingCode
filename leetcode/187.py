# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-08 18:33:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-08 18:34:20

"""
187. Repeated DNA Sequences
Medium

1471

365

Add to List

Share
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
Accepted 227,679 Submissions 531,519
"""


class Solution:
    MODS = 10 ** 9 + 7
    VS = {jj: ii for ii, jj in enumerate("ACGT")}

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, has = set(), set()
        N = len(s)
        tmp, idx = 0, 0
        while idx < N and idx < 10:
            tmp = (tmp * 4 + self.VS[s[idx]]) % self.MODS
            idx += 1
        for ii in range(N - 9):
            if ii > 0:
                tmp -= self.VS[s[ii - 1]] * (4 ** 9)
                tmp = (tmp * 4 + self.VS[s[ii + 9]]) % self.MODS
            # print(tmp)
            if tmp in has:
                res.add(s[ii : ii + 10])
            has.add(tmp)
        return list(res)