# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 10:18:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 10:29:08

"""
125. Valid Palindrome Easy
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

## Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

## Example 2:
Input: "race a car"
Output: false
Accepted 510,296 Submissions 1,480,486
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        left, right = 0, N - 1
        while left < right and left < N and left >= 0:
            while not s[left].isdigit() and not s[left].isalpha() and left < N - 1:
                left += 1
            while not s[right].isdigit() and not s[right].isalpha() and right > 0:
                right -= 1
            if left >= right:
                break
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
