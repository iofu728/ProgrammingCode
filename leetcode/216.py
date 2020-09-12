# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-11 10:03:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-11 10:04:10

"""
216. Combination Sum III Medium
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
Accepted 174,567 Submissions 306,481
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(begin: int, now: list, resave: int):
            if len(now) == k:
                if resave == 0:
                    res.append(now)
                return
            if begin > resave or begin >= 10:
                return
            dfs(begin + 1, now + [begin], resave - begin)
            dfs(begin + 1, now, resave)
        res = []
        dfs(1, [], n)
        return res
