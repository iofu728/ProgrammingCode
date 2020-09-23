# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-22 00:18:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-22 00:22:06

"""
882. Reachable Nodes In Subdivided Graph Hard
Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.

The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

and n is the total number of new nodes on that edge. 

Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

Now, you start at node 0 from the original graph, and in each move, you travel along one edge. 

Return how many nodes you can reach in at most M moves.

 

Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
Output: 13
Explanation: 
The nodes that are reachable in the final graph after M = 6 moves are indicated below.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
Output: 23
 

Note:

0 <= edges.length <= 10000
0 <= edges[i][0] < edges[i][1] < N
There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
The original graph has no parallel edges.
0 <= edges[i][2] <= 10000
0 <= M <= 10^9
1 <= N <= 3000
A reachable node is a node that can be travelled to using at most M moves starting from node 0.
 
Accepted 6,174 Submissions 14,808
"""
from collections import defaultdict
import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = defaultdict(dict)
        for ii, jj, kk in edges:
            g[ii][jj] = g[jj][ii] = kk
        queue, flag = [(0, 0)], {0: 0}
        used = {}
        res = 0
        while queue:
            d, head = heapq.heappop(queue)
            # print(d, head)
            if d > flag.get(head):
                continue
            res += 1
            for kk, vv in g[head].items():
                v = min(vv, M - d)
                used[(head, kk)] = v
                now_d = d + vv + 1
                if now_d < flag.get(kk, M + 1):
                    heapq.heappush(queue, (now_d, kk))
                    flag[kk] = now_d

        for ii, jj, kk in edges:
            res += min(kk, used.get((ii, jj), 0) + used.get((jj, ii), 0))
        return res
