# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-03 12:11:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-03 12:11:36

"""
100018. 边权重均等查询 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数4
题目难度Hard
现有一棵由 n 个节点组成的无向树，节点按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi, wi] 表示树中存在一条位于节点 ui 和节点 vi 之间、权重为 wi 的边。

另给你一个长度为 m 的二维整数数组 queries ，其中 queries[i] = [ai, bi] 。对于每条查询，请你找出使从 ai 到 bi 路径上每条边的权重相等所需的 最小操作次数 。在一次操作中，你可以选择树上的任意一条边，并将其权重更改为任意值。

注意：

查询之间 相互独立 的，这意味着每条新的查询时，树都会回到 初始状态 。
从 ai 到 bi的路径是一个由 不同 节点组成的序列，从节点 ai 开始，到节点 bi 结束，且序列中相邻的两个节点在树中共享一条边。
返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 条查询的答案。

 

示例 1：


输入：n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
输出：[0,0,1,3]
解释：第 1 条查询，从节点 0 到节点 3 的路径中的所有边的权重都是 1 。因此，答案为 0 。
第 2 条查询，从节点 3 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 0 。
第 3 条查询，将边 [2,3] 的权重变更为 2 。在这次操作之后，从节点 2 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 1 。
第 4 条查询，将边 [0,1]、[1,2]、[2,3] 的权重变更为 2 。在这次操作之后，从节点 0 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 3 。
对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。
示例 2：


输入：n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
输出：[1,2,2,3]
解释：第 1 条查询，将边 [1,3] 的权重变更为 6 。在这次操作之后，从节点 4 到节点 6 的路径中的所有边的权重都是 6 。因此，答案为 1 。
第 2 条查询，将边 [0,3]、[3,1] 的权重变更为 6 。在这次操作之后，从节点 0 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 2 。
第 3 条查询，将边 [1,3]、[5,2] 的权重变更为 6 。在这次操作之后，从节点 6 到节点 5 的路径中的所有边的权重都是 6 。因此，答案为 2 。
第 4 条查询，将边 [0,7]、[0,3]、[1,3] 的权重变更为 6 。在这次操作之后，从节点 7 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 3 。
对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。 
 

提示：

1 <= n <= 104
edges.length == n - 1
edges[i].length == 3
0 <= ui, vi < n
1 <= wi <= 26
生成的输入满足 edges 表示一棵有效的树
1 <= queries.length == m <= 2 * 104
queries[i].length == 2
0 <= ai, bi < n
"""
class Solution:
    def minOperationsQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w - 1))
            g[v].append((u, w - 1))
        q = Deque()
        q.append(0)
        par = [0] * n
        pw = [0] * n
        dep = [0] * n
        sum = [None for _ in range(n)]
        f = [[0] * 14 for _ in range(n)]
        sum[0] = [0] * 26
        while len(q):
            u = q.popleft()
            f[u][0] = par[u]
            for i in range(1, 14):
                f[u][i] = f[f[u][i - 1]][i - 1]
            for v, w in g[u]:
                if par[u] != v:
                    par[v] = u
                    sum[v] = sum[u].copy()
                    sum[v][w] += 1
                    dep[v] = dep[u] + 1
                    q.append(v)
        ans = []
        for u, v in queries:
            x, y = u, v
            if dep[x] > dep[y]:
                x, y = y, x
            for i in reversed(range(14)):
                if dep[y] - dep[x] >= 1 << i:
                    y = f[y][i]
            for i in reversed(range(14)):
                if f[x][i] != f[y][i]:
                    x, y = f[x][i], f[y][i]
            if x != y:
                x = par[x]
            ans.append(
                dep[u]
                + dep[v]
                - 2 * dep[x]
                - max([sum[u][i] + sum[v][i] - 2 * sum[x][i] for i in range(26)])
            )
        return ans