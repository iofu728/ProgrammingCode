# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 14:41:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 14:42:26

"""
390. Elimination Game Medium
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
Accepted 33,027 Submissions 74,227
"""
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))