# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 21:36:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 21:36:52

"""
947. Most Stones Removed with Same Row or Column Medium
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
Accepted 56,782 Submissions 102,826
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def get_root(r, p):
            q = r[p]
            while r[p] != p:
                p = r[p]
            while q != r[p]:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p

        r = list(range(20000))
        for ii, jj in stones:
            u, v = get_root(r, ii), get_root(r, jj + 10000)
            r[u] = v
        # print(r)
        return len(stones) - len(set([get_root(r, ii) for ii, jj in stones]))
