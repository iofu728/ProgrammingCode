# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-17 23:51:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-17 23:52:42

"""
685. Redundant Connection II Hard
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
Accepted 36,722 Submissions 112,745
"""
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def get_root(r: list, p: int):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
        N = len(edges)
        r = list(range(N + 1))
        rr = list(range(N + 1))
        cycle, flag = -1, -1
        for idx, (ii, jj) in enumerate(edges):
            if r[jj] != jj:
                flag = idx
            else:
                r[jj] = ii
                u, v = get_root(rr, ii), get_root(rr, jj)
                if u == v:
                    cycle = idx
                else:
                    rr[u] = v
        if flag < 0:
            return edges[cycle]

        tmp = edges[flag]
        if cycle < 0:
            return tmp
        return [r[tmp[1]], tmp[1]] 