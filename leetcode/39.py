# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-31 22:13:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-31 22:14:44

"""
39. Combination Sum Medium
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
Accepted 549,965 Submissions 983,999
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, path, t):
            if not t:
                res.append(path.copy())
                return
            for ii in range(idx, N):
                tmp = t - candidates[ii]
                if tmp < 0:
                    break
                path.append(candidates[ii])
                dfs(ii, path, tmp)
                path.pop()

        N = len(candidates)
        if not N:
            return []
        candidates.sort()
        path, res = [], []
        dfs(0, path, target)
        return res
