# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-01 22:31:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-01 22:33:08

"""
984. String Without AAA or BBB Medium
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
Accepted 17,666 Submissions 47,148
"""
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = []
        while A > 0 or B > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                is_a = res[-1] == "b"
            else:
                is_a = A >= B
            if is_a:
                A -= 1
                res.append("a")
            else:
                B -= 1
                res.append("b")
        return "".join(res)
