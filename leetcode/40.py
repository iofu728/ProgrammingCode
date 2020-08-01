# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-31 22:36:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-31 22:36:59

"""
40. Combination Sum II Medium
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
Accepted 331,620 Submissions 691,231
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(c: list, now: list, t: int, flag: int = 0):
            # print(flag, c, now, t)
            if t == 0:
                res.add(tuple(now.copy()))
                return
            if not len(c):
                return
            tmp = c[0]
            if tmp <= t:
                dfs(c[1:], now + [tmp], t - tmp)
            dfs(c[1:], now, t, 1)

        candidates = [ii for ii in candidates if ii <= target]
        N = len(candidates)
        if not N:
            return []
        candidates.sort()
        path, res = [], set()
        dfs(candidates, [], target)
        return [list(ii) for ii in res]
