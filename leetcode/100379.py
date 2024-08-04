# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-04 12:52:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-04 12:52:57

"""
100379. 新增道路查询后的最短距离 I 显示英文描述 
通过的用户数4
尝试过的用户数6
用户总通过次数4
用户总提交次数6
题目难度Medium
给你一个整数 n 和一个二维整数数组 queries。

有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。

queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。

返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。

 

示例 1：

输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]

输出： [3, 2, 1]

解释：



新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。



新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。



新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。

示例 2：

输入： n = 4, queries = [[0, 3], [0, 2]]

输出： [1, 1]

解释：



新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。



新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。

 

提示：

3 <= n <= 500
1 <= queries.length <= 500
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
查询中没有重复的道路。
"""
def dijkstras(n: int, source: int, destination: int, g):
    START_NODE = source
    distances = [inf] * n
    distances[START_NODE] = 0 
    heap = [(0, START_NODE)]
    while heap:
        cur_dist, cur_node = heappop(heap)
        if cur_node == destination:
            return cur_dist

        if cur_dist > distances[cur_node]:
            continue

        for nei in g[cur_node]:
            dist = cur_dist + 1
            if dist < distances[nei]:
                distances[nei] = dist
                heappush(heap, (dist, nei))
    return inf

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        g = defaultdict(list)
        for ii in range(n - 1):
            g[ii].append(ii + 1)
        for ii, jj in queries:
            g[ii].append(jj)
            res.append(dijkstras(n, 0, n - 1, g))
        return res