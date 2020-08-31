# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 15:01:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 15:01:36

"""
面试题 04.01. 节点间通路
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。
通过次数6,242提交次数11,795
"""


class Solution:
    def findWhetherExistsPath(
        self, n: int, graph: List[List[int]], start: int, target: int
    ) -> bool:
        def dfs(u):
            dp[u] = 1
            if self.res:
                return
            if u == target:
                self.res = True
            for v in g[u]:
                if not dp[v]:
                    dfs(v)

        dp = [0] * n
        g = {ii: [] for ii in range(n)}
        self.res = False
        for ii, jj in graph:
            g[ii].append(jj)
        dfs(start)
        return self.res
