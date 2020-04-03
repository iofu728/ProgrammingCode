# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 20:24:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 20:25:23

"""
6. ZigZag Conversion Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

## Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

## Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

Accepted 424,795 Submissions 1,211,251
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        N = len(s)
        rows = [""] * min(numRows, N)
        curRow, goingDown = 0, False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        return "".join(rows)
