# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 23:19:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 23:21:10

"""
1138. Alphabet Board Path Medium
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
Accepted 14,848 Submissions 30,600
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def get_id(s: str):
            s = ord(s) - ord("a")
            x, y = s // 5, s % 5
            return x, y

        def get_d(x: int, y: int):
            if x > 0:
                tmp1 = "D" * x
            elif x < 0:
                tmp1 = "U" * (-x)
            else:
                tmp1 = ""
            if y > 0:
                tmp2 = "R" * y
            elif y < 0:
                tmp2 = "L" * (-y)
            else:
                tmp2 = ""
            if x > 0:
                return tmp2 + tmp1 + "!"
            return tmp1 + tmp2 + "!"

        N = len(target)
        if not N:
            return ""
        res = get_d(*get_id(target[0]))
        for ii in range(1, N):
            a = get_id(target[ii])
            b = get_id(target[ii - 1])
            res += get_d(a[0] - b[0], a[1] - b[1])
        return res
