# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-20 12:55:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-20 23:35:39

"""
1192. Critical Connections in a Network
Hard

1835

101

Add to List

Share
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
Accepted
87,358
Submissions
176,061
"""

from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(idx, father, depth):
            if ids[idx] >= 0:
                return ids[idx]
            ids[idx] = depth
            m_depth  = n
            for ii in g[idx]:
                if ii == father:
                    continue
                sub_depth =  dfs(ii, idx, depth + 1)
                if sub_depth <= depth:
                    connections.discard(tuple(sorted((idx, ii))))
                m_depth = min(sub_depth, m_depth)
            return m_depth

        g = defaultdict(list)
        for ii, jj in connections:
            g[ii].append(jj)
            g[jj].append(ii)
        ids = [-1] * n
        connections = set([tuple(sorted((ii, jj))) for ii, jj in connections])
        dfs(0, -1, 0)
        return list(connections)