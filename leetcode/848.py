# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 10:50:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 10:51:23

"""
848. Shifting Letters Medium
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
Accepted 25,407 Submissions 56,808
"""


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        suffix, N = [], len(S)
        for ii in range(N - 1, -1, -1):
            tmp = (shifts[ii] + (0 if (ii == N - 1) else suffix[0])) % 26
            suffix.insert(0, tmp)
        res = ""
        for ii, jj in zip(S, suffix):
            tmp = ord(ii) + jj
            if tmp > ord("z"):
                tmp -= 26
            res += chr(tmp)
        return res
