# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-21 10:58:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-21 10:58:50

"""
100276. 最短路径中的边 显示英文描述 
通过的用户数5
尝试过的用户数6
用户总通过次数5
用户总提交次数8
题目难度Hard
给你一个 n 个节点的无向带权图，节点编号为 0 到 n - 1 。图中总共有 m 条边，用二维数组 edges 表示，其中 edges[i] = [ai, bi, wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。

对于节点 0 为出发点，节点 n - 1 为结束点的所有最短路，你需要返回一个长度为 m 的 boolean 数组 answer ，如果 edges[i] 至少 在其中一条最短路上，那么 answer[i] 为 true ，否则 answer[i] 为 false 。

请你返回数组 answer 。

注意，图可能不连通。

 

示例 1：



输入：n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]

输出：[true,true,true,false,true,true,true,false]

解释：

以下为节点 0 出发到达节点 5 的 所有 最短路：

路径 0 -> 1 -> 5 ：边权和为 4 + 1 = 5 。
路径 0 -> 2 -> 3 -> 5 ：边权和为 1 + 1 + 3 = 5 。
路径 0 -> 2 -> 3 -> 1 -> 5 ：边权和为 1 + 1 + 2 + 1 = 5 。
示例 2：



输入：n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]

输出：[true,false,false,true]

解释：

只有一条从节点 0 出发到达节点 3 的最短路 0 -> 2 -> 3 ，边权和为 1 + 2 = 3 。

 

提示：

2 <= n <= 5 * 104
m == edges.length
1 <= m <= min(5 * 104, n * (n - 1) / 2)
0 <= ai, bi < n
ai != bi
1 <= wi <= 105
图中没有重边。
"""
def dijkstra_all_paths(graph, start_vertex):
    # The distances dictionary stores the minimum distance from start_vertex to each other vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    
    # Priority queue to retrieve the vertex with the smallest distance
    priority_queue = [(0, start_vertex)]
    
    # To store the predecessors for each vertex that are part of the shortest path
    predecessors = {vertex: [] for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Explore each adjacent vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Found a new shortest path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = [current_vertex]
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor]:
                # Another shortest path found, add the predecessor
                predecessors[neighbor].append(current_vertex)
    
    return distances, predecessors

def find_paths(predecessors, end_vertex):
    def backtrack(current_vertex):
        if not predecessors.get(current_vertex, []):  # Base case: start vertex
            return [[current_vertex]]
        paths = []
        for pred in predecessors[current_vertex]:
            for path in backtrack(pred):
                paths.append(path + [current_vertex])
        return paths
    
    return backtrack(end_vertex)

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(dict)
        edges_map = {}
        for idx, (ii, jj, kk) in enumerate(edges):
            graph[ii][jj] = kk
            graph[jj][ii] = kk
            if ii > jj:
                ii, jj = jj, ii
            edges_map[(ii, jj)] = idx
        distances, predecessors = dijkstra_all_paths(graph, 0)
        paths = find_paths(predecessors, n - 1)
        res = [False] * len(edges)
        for path in paths:
            for k in range(1, len(path)):
                ii, jj = path[k - 1], path[k]
                if ii > jj:
                    ii, jj = jj, ii
                res[edges_map[(ii, jj)]] = True
        return res   
