# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-05-21 12:21:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-05-21 12:21:35

"""
6442. 修改图中的边权 显示英文描述 
通过的用户数65
尝试过的用户数498
用户总通过次数88
用户总提交次数1431
题目难度Hard
给你一个 n 个节点的 无向带权连通 图，节点编号为 0 到 n - 1 ，再给你一个整数数组 edges ，其中 edges[i] = [ai, bi, wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。

部分边的边权为 -1（wi = -1），其他边的边权都为 正 数（wi > 0）。

你需要将所有边权为 -1 的边都修改为范围 [1, 2 * 109] 中的 正整数 ，使得从节点 source 到节点 destination 的 最短距离 为整数 target 。如果有 多种 修改方案可以使 source 和 destination 之间的最短距离等于 target ，你可以返回任意一种方案。

如果存在使 source 到 destination 最短距离为 target 的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。如果不存在这样的方案，请你返回一个 空数组 。

注意：你不能修改一开始边权为正数的边。

 

示例 1：



输入：n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
输出：[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
解释：上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。
示例 2：



输入：n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
输出：[]
解释：上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个空数组。
示例 3：



输入：n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
输出：[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
解释：上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。
 

提示：

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 或者 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
输入的图是连通图，且没有自环和重边。
"""
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(set)
        for x, y, z in edges:
            graph[x].add((y, z))
            graph[y].add((x, z))
            
        def impossible(n: int, source: int, destination: int, target: int):
            START_NODE = source
            distances = [inf] * n
            distances[START_NODE] = 0 
            heap = [(0, START_NODE)]
            while heap:
                cur_dist, cur_node = heappop(heap)
                if cur_dist > distances[cur_node]:
                    continue
                for nei, w in graph[cur_node]:
                    if w == -1:
                        continue
                    dist = cur_dist + w
                    if dist < distances[nei]:
                        distances[nei] = dist
                        heappush(heap, (dist, nei))

            if distances[destination] < target:
                return True

            START_NODE = source
            distances = [inf] * n
            distances[START_NODE] = 0 
            heap = [(0, START_NODE)]
            while heap:
                cur_dist, cur_node = heappop(heap)
                if cur_dist > distances[cur_node]:
                    continue
                for nei, w in graph[cur_node]:
                    if w == -1:
                        w = 1

                    dist = cur_dist + w
                    if dist < distances[nei]:
                        distances[nei] = dist
                        heappush(heap, (dist, nei))
                        
            if distances[destination] > target:
                return True
            
            return False
        
        if impossible(n, source, destination, target):
            return []
        
        def dijkstras(n: int, source: int, destination: int):
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

                for nei, w in graph[cur_node]:
                    dist = cur_dist + w
                    if dist < distances[nei]:
                        distances[nei] = dist
                        heappush(heap, (dist, nei))

            return inf
        
        e = []
        for x, y, z in edges:
            if z == -1:
                graph[x].remove((y, z))
                graph[y].remove((x, z))
                graph[x].add((y, 1))
                graph[y].add((x, 1))
    
        for x, y, z in edges:
            if z != -1:
                continue
        
            graph[x].remove((y, 1))
            graph[y].remove((x, 1))
            graph[x].add((y, 10 ** 9))
            graph[y].add((x, 10 ** 9))
            
            if dijkstras(n, source, destination) > target:
                e = [x, y, z]
                graph[x].remove((y, 10 ** 9))
                graph[y].remove((x, 10 ** 9))
                graph[x].add((y, 1))
                graph[y].add((x, 1))
                
        
        d = target - dijkstras(n, source, destination)
        if e:
            e[-1] = 1 + d
            graph[e[0]].remove((e[1], 1))
            graph[e[1]].remove((e[0], 1))
            graph[e[0]].add((e[1], e[-1]))
            graph[e[1]].add((e[0], e[-1]))
        
        ans = set()
        for x in graph:
            for y, z in graph[x]:
                ans.add((min(x, y), max(x, y), z))
        
        res = []
        for x, y, z in ans:
            res.append([x, y, z])
        
        return res