# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-02 01:26:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-02 01:27:48

"""
394. Decode String Medium
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
Accepted 227,479 Submissions 452,167
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[1, []]]
        idx, N = 0, len(s)
        while idx < N:
            if s[idx].isdigit():
                print(idx)
                b = idx
                while idx < N and s[idx + 1].isdigit():
                    idx += 1
                num = int(s[b : idx + 1])
                stack.append([num, []])
            elif s[idx] == "]":
                num, t = stack.pop(-1)
                one = "".join([ii * jj for ii, jj in t])
                stack[-1][1].append([one, num])
            elif s[idx] == "[":
                if idx == 0 or not s[idx - 1].isdigit():
                    stack.append([1, []])
            else:
                t = s[idx]
                num = 1
                stack[-1][1].append([t, num])
            # print(idx, s[idx], stack)
            idx += 1
        # print(stack)
        num, t = stack.pop(-1)
        return "".join([ii * jj for ii, jj in t]) * num
