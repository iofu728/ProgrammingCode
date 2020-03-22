# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 19:51:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 19:52:25

"""
89. Gray Code Medium

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

## Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

## Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

Accepted 154,105 Submissions 320,925
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        result = []
        nums = set()

        def dfs(num: List[str]):
            nums.add("".join(num))
            result.append(int("".join(num), 2))
            if len(result) == 2 ** n:
                return
            for idx, ii in enumerate(num):
                new = num[:idx] + ["1" if ii == "0" else "0"] + num[idx + 1 :]
                if "".join(new) not in nums:
                    dfs(new)
                    break

        dfs(["0"] * n)
        return result
