# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 11:10:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 12:13:49

"""
5510. 保证图可完全遍历 显示英文描述 
通过的用户数79
尝试过的用户数110
用户总通过次数81
用户总提交次数142
题目难度Hard
Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

类型 1：只能由 Alice 遍历。
类型 2：只能由 Bob 遍历。
类型 3：Alice 和 Bob 都可以遍历。
给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

 

示例 1：



输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
示例 2：



输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
输出：0
解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
示例 3：



输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
输出：-1
解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。
 

提示：

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
所有元组 (typei, ui, vi) 互不相同
"""


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def getroot(r, p):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p

        ra = list(range(n))
        e = [[], [], []]
        for types, u, v in edges:
            e[types - 1].append((u - 1, v - 1))
        ans = 0
        for u, v in e[2]:
            u, v = getroot(ra, u), getroot(ra, v)
            if u == v:
                ans += 1
            else:
                ra[u] = v
        rb = ra.copy()
        for el, r in ((e[0], ra), (e[1], rb)):
            for u, v in el:
                u, v = getroot(r, u), getroot(r, v)
                if u == v:
                    ans += 1
                else:
                    r[u] = v
            r0 = getroot(r, 0)
            for i in range(1, n):
                if getroot(r, i) != r0:
                    return -1
        return ans


# from collections import defaultdict
# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         def kruskal(g, N, types):
#             def get_edgenum():
#                 count = 0
#                 for ii in range(1, N + 1):
#                     for jj in range(ii + 1, N + 1):
#                         count += len([kk for kk in g[ii][jj] if kk in [3, types]]) > 0
#                 return count

#             res = []
#             M = get_edgenum()
#             if N <= 0 or M < N - 1:
#                 # print(M, N)
#                 return -1
#             edge_list = []
#             for ii in range(N):
#                 for jj in range(ii, N):
#                     for kk in [kk for kk in g[ii][jj] if kk in [3, types]]:
#                         edge_list.append([ii, jj, kk])
#             edge_list.sort(key=lambda a:-a[2])

#             group = [[ii] for ii in range(N)]
#             ans = 0
#             for edge in edge_list:
#                 for ii in range(len(group)):
#                     if edge[0] in group[ii]:
#                         m = ii
#                     if edge[1] in group[ii]:
#                         n = ii
#                 if m != n:
#                     res.append(edge)
#                     group[m] = group[m] + group[n]
#                     group[n] = []
#                 else:
#                     ans += 1
#                     # print("======", edge)
#             return ans

#         g = [defaultdict(list) for _ in range(n + 1)]
#         res = 0
#         for types, ii, jj in edges:
#             g[ii][jj].append(types)
#             g[jj][ii].append(types)
#         for ii, t1 in enumerate(g):
#             for jj, t2 in t1.items():
#                 if jj < ii:
#                     continue
#                 if 3 in t2 and (1 in t2 or 2 in t2):
#                     res += len(t2) - 1
#                     g[ii][jj] = [3]
#                     g[jj][ii] = [3]
#         a1 = kruskal(g, n, 1)
#         a2 = kruskal(g, n, 2)
#         if -1 in [a1, a2]:
#             return -1
#         return res + a1 + a2
