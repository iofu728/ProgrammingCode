# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 19:50:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 19:50:59

"""
842. Split Array into Fibonacci Sequence Medium
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
Accepted 20,486 Submissions 56,393
"""


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def dfs(ii: int, jj: int) -> bool:
            # print(ii, jj)
            a, b = S[:ii], S[ii : ii + jj]
            if (
                (len(b) > 1 and b[0] == "0")
                or (len(a) > 1 and a[0] == "0")
                or not len(b)
                or not len(a)
                or ii + jj == N
            ):
                return False
            a, b, pre = int(a), int(b), ii + jj
            tmp = [a, b]
            while pre < N:
                a, b = b, a + b
                tmp.append(b)
                c_len = len(str(b))
                c_s = S[pre : pre + c_len]
                # print(a, b, c_s)
                if b != int(c_s) or (c_len > 1 and c_s[0] == "0") or b >= 2 ** 31:
                    return False
                pre += c_len
            return tmp

        N = len(S)
        for ii in range(1, N // 3 + 2):
            for jj in range(1, (N - ii) // 2 + 2):
                tmp = dfs(ii, jj)
                if not tmp is False:
                    return tmp
        return []
