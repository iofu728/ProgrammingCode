# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-28 21:48:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-28 21:48:49

"""
96. Unique Binary Search Trees Medium
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19
Accepted 323,175 Submissions 605,462
"""


class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1
        for ii in range(2, n + 1):
            G[ii] = sum([G[jj - 1] * G[ii - jj] for jj in range(1, ii + 1)])
        return G[-1]
