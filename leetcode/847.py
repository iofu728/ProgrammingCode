"""
847. Shortest Path Visiting All Nodes
Hard

1383

102

Add to List

Share
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
Accepted
33,734
Submissions
59,671
"""


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        END = (1 << N) - 1
        q = deque((1 << ii, ii) for ii in range(N))
        res = defaultdict(lambda: N * N)
        for ii in range(N):
            res[1 << ii, ii] = 0
        while q:
            mask, head = q.popleft()
            d = res[mask, head]
            if mask == END:
                return d
            for jj in graph[head]:
                m = mask | (1 << jj)
                if d + 1 < res[m, jj]:
                    res[m, jj] = d + 1
                    q.append((m, jj))
