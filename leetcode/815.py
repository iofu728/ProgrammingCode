# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 20:46:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 20:47:18

"""
815. Bus Routes Hard
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
Accepted 39,483 Submissions 92,475
"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        N = len(routes)
        if S == T:
            return 0
        routes = list(map(set, routes))
        g = [set() for _ in range(N)]
        for ii, r1 in enumerate(routes):
            for jj in range(ii + 1, N):
                r2 = routes[jj]
                if any([1 for kk in r2 if kk in r1]):
                    g[ii].add(jj)
                    g[jj].add(ii)
        ss, tt = set(), set()
        for ii, jj in enumerate(routes):
            if S in jj:
                ss.add(ii)
            if T in jj:
                tt.add(ii)
        queue = [(ii, 1) for ii in ss]
        for ii, jj in queue:
            if ii in tt:
                return jj
            for kk in g[ii]:
                if kk not in ss:
                    ss.add(kk)
                    queue.append((kk, jj + 1))
        return -1
