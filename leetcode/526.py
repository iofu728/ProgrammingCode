# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 18:47:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 19:26:37

"""
526. Beautiful Arrangement Medium
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

## Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

## Note:

N is a positive integer and will not exceed 15.

Accepted 46,600 Submissions 81,841
"""


class Solution:
    def countArrangement(self, N: int) -> int:
        self.res = 0

        def dfs(have: list, tmp: list):
            if not len(have):
                self.res += 1
            T = len(tmp) + 1
            for idx, ii in enumerate(have):
                # print(have, tmp, T, ii)
                if not T % ii or not ii % T:
                    dfs(have[:idx] + have[idx + 1 :], tmp + [ii])

        dfs(list(range(1, N + 1)), [])
        return self.res
