# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 22:34:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 23:34:06

"""
14. Longest Common Prefix Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

## Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## Note:
All given inputs are in lowercase letters a-z.

Accepted 669,168 Submissions 1,923,748
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        if N == 1:
            return strs[0]
        if not N:
            return ""

        def get_prefix(a: str, b: str) -> str:
            result = []
            for ii in range(min(len(a), len(b))):
                if a[ii] != b[ii]:
                    return a[:ii]
            return a[: min(len(a), len(b))]

        result = get_prefix(strs[0], strs[1])
        for ii in range(2, N):
            result = get_prefix(result, strs[ii])
            if result == "":
                return ""
        return result
