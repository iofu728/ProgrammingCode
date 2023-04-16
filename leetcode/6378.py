# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-04-16 12:08:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-04-16 12:08:51

"""
6378. 最小化旅行的价格总和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。

每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。

给定路径的 价格总和 是该路径上所有节点的价格之和。

另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 endi 。

在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。

返回执行所有旅行的最小价格总和。

 

示例 1：


输入：n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
输出：23
解释：
上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。
示例 2：


输入：n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
输出：1
解释：
上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 
第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 
所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
 

提示：

1 <= n <= 50
edges.length == n - 1
0 <= ai, bi <= n - 1
edges 表示一棵有效的树
price.length == n
price[i] 是一个偶数
1 <= price[i] <= 1000
1 <= trips.length <= 100
0 <= starti, endi <= n - 1
"""
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        path = [[] for _ in range(n)]
        for u, v in edges:
            path[u].append(v)
            path[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        stack = [(-1, 0)]
        tree = [[] for _ in range(n)]
        while stack:
            p, u = stack.pop()
            for v in path[u]:
                if v != p:
                    tree[u].append(v)
                    parent[v] = u
                    stack.append((u, v))
                    depth[v] = depth[u] + 1
        weight = [0] * n
        for u, v in trips:
            if depth[u] > depth[v]:
                u, v = v, u
            while depth[u] != depth[v]:
                weight[v] += 1
                v = parent[v]
            while u != v:
                weight[u] += 1
                weight[v] += 1
                u = parent[u]
                v = parent[v]
            weight[u] += 1

        def dfs(u):
            tmp0, tmp1 = 0, weight[u] * price[u] // 2
            for v in tree[u]:
                x0, x1 = dfs(v)
                tmp0 += max(x0, x1)
                tmp1 += x0
            return tmp0, tmp1
        res0, res1 = dfs(0)
        tot = sum(x * y for x, y in zip(price, weight))
        return tot - max(res0, res1)