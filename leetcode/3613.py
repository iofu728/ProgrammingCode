"""
3613. 最小化连通分量的最大成本
已解答
中等
premium lock icon
相关企业
提示
给你一个无向连通图，包含 n 个节点，节点编号从 0 到 n - 1，以及一个二维整数数组 edges，其中 edges[i] = [ui, vi, wi] 表示一条连接节点 ui 和节点 vi 的无向边，边权为 wi，另有一个整数 k。

你可以从图中移除任意数量的边，使得最终的图中 最多 只包含 k 个连通分量。

连通分量的 成本 定义为该分量中边权的 最大值 。如果一个连通分量没有边，则其代价为 0。

请返回在移除这些边之后，在所有连通分量之中的 最大成本 的 最小可能值 。

 

示例 1：

输入： n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2

输出： 4

解释：



移除节点 3 和节点 4 之间的边（权值为 6）。
最终的连通分量成本分别为 0 和 4，因此最大代价为 4。
示例 2：

输入： n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1

输出： 5

解释：



无法移除任何边，因为只允许一个连通分量（k = 1），图必须保持完全连通。
该连通分量的成本等于其最大边权，即 5。
 

提示：

1 <= n <= 5 * 104
0 <= edges.length <= 105
edges[i].length == 3
0 <= ui, vi < n
1 <= wi <= 106
1 <= k <= n
输入图是连通图。
"""
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        def get_father(r, p):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
        def is_ok(t):
            ra = list(range(n))
            for i, j, x in edges:
                if x <= t:
                    i, j = get_father(ra, i), get_father(ra, j)
                    ra[i] = j
            return len(set([get_father(ra, i) for i in range(n)])) <= k

        left = 0
        right = max([i[-1] for i in edges]) + 1 if edges else 0
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid
            else:
                left = mid + 1
        return left



