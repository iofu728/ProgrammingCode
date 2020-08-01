# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-12 10:42:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-12 20:57:08

"""
5211. 概率最大的路径 显示英文描述 
通过的用户数685
尝试过的用户数2041
用户总通过次数705
用户总提交次数5911
题目难度Medium
给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。

指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。

示例 1：

输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
输出：0.25000
解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
示例 2：

输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
输出：0.30000
示例 3：

输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
输出：0.00000
解释：节点 0 和 节点 2 之间不存在路径

提示：

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
每两个节点之间最多有一条边
"""
import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        maps, weight = {i: [] for i in range(n)}, {}
        for (ii, jj), kk in zip(edges, succProb):
            maps[ii].append(jj)
            maps[jj].append(ii)
            weight[(ii, jj)] = kk
            weight[(jj, ii)] = kk
        queue = []
        heapq.heappush(queue, (-1, start))
        maxRate = [0 for _ in range(n)]
        maxRate[start] = 1
        fixed = set()

        while queue:
            now_rate, node = heapq.heappop(queue)
            if node in fixed:
                continue
            fixed.add(node)
            if node == end:
                return maxRate[end]
            for ii in maps[node]:
                if -1 * now_rate * weight[(node, ii)] > maxRate[ii]:
                    maxRate[ii] = -1 * now_rate * weight[(node, ii)]
                    heapq.heappush(queue, (-1 * maxRate[ii], ii))
        return 0
