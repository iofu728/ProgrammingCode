# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-30 11:53:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-30 11:54:04

"""
100318. 合并两棵树后的最小直径 显示英文描述 
通过的用户数42
尝试过的用户数73
用户总通过次数44
用户总提交次数122
题目难度Hard
给你两棵 无向 树，分别有 n 和 m 个节点，节点编号分别为 0 到 n - 1 和 0 到 m - 1 。给你两个二维整数数组 edges1 和 edges2 ，长度分别为 n - 1 和 m - 1 ，其中 edges1[i] = [ai, bi] 表示在第一棵树中节点 ai 和 bi 之间有一条边，edges2[i] = [ui, vi] 表示在第二棵树中节点 ui 和 vi 之间有一条边。

你必须在第一棵树和第二棵树中分别选一个节点，并用一条边连接它们。

请你返回添加边后得到的树中，最小直径 为多少。

一棵树的 直径 指的是树中任意两个节点之间的最长路径长度。

 

示例 1：

输入：edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

输出：3

解释：

将第一棵树中的节点 0 与第二棵树中的任意节点连接，得到一棵直径为 3 得树。

示例 2：

输入：edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

输出：5

解释：

将第一棵树中的节点 0 和第二棵树中的节点 0 连接，可以得到一棵直径为 5 的树。

 

提示：

1 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
输入保证 edges1 和 edges2 分别表示一棵合法的树。
"""
from collections import deque, defaultdict

def tree_diameter(edges, n):
    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        q = deque([start])
        farthest_node = start
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
                    farthest_node = neighbor
        return farthest_node, dist

    # Build graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find one endpoint of the diameter
    farthest_node, _ = bfs(0)
    # Find the other endpoint of the diameter
    other_end, dist = bfs(farthest_node)
    
    diameter = dist[other_end]
    return diameter

def min_diameter_after_merge(edges1, edges2):
    diameter1 = tree_diameter(edges1, len(edges1) + 1)
    diameter2 = tree_diameter(edges2, len(edges2) + 1)
    print(diameter1, diameter2)
    
    new_diameter = max(diameter1, diameter2, math.ceil(diameter1 / 2) + 1 + math.ceil(diameter2 / 2))
    
    return new_diameter


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        return min_diameter_after_merge(edges1, edges2)
