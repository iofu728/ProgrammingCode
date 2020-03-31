# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-31 22:15:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-31 22:16:15

"""
1328. Break a Palindrome Medium
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

## Example 1:
Input: palindrome = "abccba"
Output: "aaccba"

## Example 2:
Input: palindrome = "a"
Output: ""

## Constraints:
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.

Accepted 5,810 Submissions 14,026
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N < 2:
            return ""
        left = 0
        while left < int(N // 2) and palindrome[left] == "a":
            left += 1
        if left >= int(N // 2):
            left = N - 1
            replace = "b"
        else:
            replace = "a"
        return palindrome[:left] + replace + palindrome[left + 1 :]
