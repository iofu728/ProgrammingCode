"""
564. Find the Closest Palindrome
Hard

457

1095

Add to List

Share
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
Accepted
30,141
Submissions
142,866
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        N = len(n)
        c = [10 ** (N - 1) - 1, 10 ** N + 1]
        p = int(n[: (N + 1) // 2])
        for ii in range(p - 1, p + 2):
            y = ii if N % 2 == 0 else ii // 10
            while y:
                ii = ii * 10 + y % 10
                y //= 10
            c.append(ii)
        res = -1
        k = int(n)
        # print(c)
        for ii in c:
            if ii != k:
                if (
                    res == -1
                    or abs(ii - k) < abs(res - k)
                    or (abs(ii - k) == abs(res - k) and ii < res)
                ):
                    res = ii
        return str(res)
