# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-08 11:13:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-08 11:42:58

"""
5355. Frog Position After T Seconds
User Accepted:887
User Tried:1404
Total Accepted:934
Total Submissions:3439
Difficulty:Hard
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from the vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.

 

Example 1:



Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:



Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
Example 3:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666
 

Constraints:

1 <= n <= 100
edges.length == n-1
edges[i].length == 2
1 <= edges[i][0], edges[i][1] <= n
1 <= t <= 50
1 <= target <= n
Answers within 10^-5 of the actual value will be accepted as correct.
"""

import heapq


class Solution:
    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        relation_map = {ii: [] for ii in range(1, n + 1)}
        for ii, jj in edges:
            relation_map[ii].append(jj)
            relation_map[jj].append(ii)
        path = []
        queue = []
        heapq.heappush(queue, (1, []))
        while len(queue) > 0:
            head, past = heapq.heappop(queue)
            if head == target:
                path = past
                break
            for ii in relation_map[head]:
                if ii not in past:
                    heapq.heappush(queue, [ii, [*past, head]])
        if self.is_zero(path, relation_map, t, target):
            return 0.0
        cost = 1.0
        for ii in path:
            num = len(relation_map[ii])
            if ii != 1:
                num -= 1
            cost *= 1 / num
        return cost

    def is_zero(self, path: list, relation_map: dict, t: int, target: int) -> bool:
        if len(path) > t:
            return True
        if len(path) < t:
            num = len(relation_map[target])
            if target != 1:
                num -= 1
            if num != 0:
                return True
        return False

