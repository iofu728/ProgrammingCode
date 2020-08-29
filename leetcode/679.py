# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-22 14:31:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-22 14:32:47

"""
679. 24 Game Hard
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
Accepted 41,593 Submissions 89,502
"""


class Solution:
    TAR = 24
    EPS = 1e-6

    def judgePoint24(self, nums: List[int]) -> bool:
        def dfs(num: list) -> bool:
            if len(num) == 1:
                return abs(num[0] - self.TAR) < self.EPS
            for ii, x in enumerate(num):
                for jj, y in enumerate(num):
                    if ii == jj:
                        continue
                    tmp = []
                    for kk, z in enumerate(num):
                        if not kk in [ii, jj]:
                            tmp.append(z)
                    for kk in range(4):
                        if kk < 2 and ii > jj:
                            continue
                        if kk == 0:
                            tmp.append(x + y)
                        elif kk == 1:
                            tmp.append(x * y)
                        elif kk == 2:
                            tmp.append(x - y)
                        elif kk == 3:
                            if abs(y) < self.EPS:
                                continue
                            tmp.append(x / y)
                        if dfs(tmp):
                            return True
                        tmp.pop()
            return False

        return dfs(nums)
