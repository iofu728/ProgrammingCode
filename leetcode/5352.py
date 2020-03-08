# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-08 10:30:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-08 10:34:44

"""
5352. Generate a String With Characters That Have Odd Counts
User Accepted:979
User Tried:1298
Total Accepted:986
Total Submissions:1379
Difficulty:Easy
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

 

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Example 3:

Input: n = 7
Output: "holasss"
 

Constraints:

1 <= n <= 500
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0 or n == 1:
            return "".join([*["a"] * (n - 1), "b"])
        return "".join([*["a"] * (n - 2), "b", "c"])

