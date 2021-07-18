# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 20:46:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-28 21:14:17

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
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        stations = defaultdict(set)
        for bus, ss in enumerate(routes):
            for s in ss:
                stations[s].add(bus)
        routes = [set(ii) for ii in routes]
        queue = [(source, 0)]
        buses, stops = set(), set([source])
        while queue:
            now, step = queue.pop(0)
            if now == target:
                return step
            for bus in stations[now] - buses:
                for s in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(s)
                    queue.append((s, step + 1))
        return -1
