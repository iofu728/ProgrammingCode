# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-08 00:40:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-08 00:41:02

"""
77. Combinations Medium
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
Accepted 305,255 Submissions 553,393
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(idx: int, now: list):
            if len(now) == k:
                res.append(now)
            for ii in range(idx, n + 1):
                dfs(ii + 1, now + [ii])

        res = []
        dfs(1, [])
        return res
