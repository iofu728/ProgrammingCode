# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-01-21 11:03:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-01-21 11:03:48

"""
100188. 按距离统计房屋对数目 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你三个 正整数 n 、x 和 y 。

在城市中，存在编号从 1 到 n 的房屋，由 n 条街道相连。对所有 1 <= i < n ，都存在一条街道连接编号为 i 的房屋与编号为 i + 1 的房屋。另存在一条街道连接编号为 x 的房屋与编号为 y 的房屋。

对于每个 k（1 <= k <= n），你需要找出所有满足要求的 房屋对 [house1, house2] ，即从 house1 到 house2 需要经过的 最少 街道数为 k 。

返回一个下标从 1 开始且长度为 n 的数组 result ，其中 result[k] 表示所有满足要求的房屋对的数量，即从一个房屋到另一个房屋需要经过的 最少 街道数为 k 。

注意，x 与 y 可以 相等 。

 

示例 1：


输入：n = 3, x = 1, y = 3
输出：[6,0,0]
解释：让我们检视每个房屋对
- 对于房屋对 (1, 2)，可以直接从房屋 1 到房屋 2。
- 对于房屋对 (2, 1)，可以直接从房屋 2 到房屋 1。
- 对于房屋对 (1, 3)，可以直接从房屋 1 到房屋 3。
- 对于房屋对 (3, 1)，可以直接从房屋 3 到房屋 1。
- 对于房屋对 (2, 3)，可以直接从房屋 2 到房屋 3。
- 对于房屋对 (3, 2)，可以直接从房屋 3 到房屋 2。
示例 2：


输入：n = 5, x = 2, y = 4
输出：[10,8,2,0,0]
解释：对于每个距离 k ，满足要求的房屋对如下：
- 对于 k == 1，满足要求的房屋对有 (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), 以及 (5, 4)。
- 对于 k == 2，满足要求的房屋对有 (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), 以及 (5, 3)。
- 对于 k == 3，满足要求的房屋对有 (1, 5)，以及 (5, 1) 。
- 对于 k == 4 和 k == 5，不存在满足要求的房屋对。
示例 3：


输入：n = 4, x = 1, y = 1
输出：[6,4,2,0]
解释：对于每个距离 k ，满足要求的房屋对如下：
- 对于 k == 1，满足要求的房屋对有 (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), 以及 (4, 3)。
- 对于 k == 2，满足要求的房屋对有 (1, 3), (3, 1), (2, 4), 以及 (4, 2)。
- 对于 k == 3，满足要求的房屋对有 (1, 4), 以及 (4, 1)。
- 对于 k == 4，不存在满足要求的房屋对。
 

提示：

2 <= n <= 100
1 <= x, y <= n
"""
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        num_vertices = n + 1
        
        # 初始化距离矩阵，设无边连接的节点距离为无穷大
        distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]

        # 对于图中的每一个顶点，其到自身的距离为0
        for i in range(1, num_vertices):
            distance[i][i] = 0

        # 根据边的信息更新距离矩阵
        for u in range(1, num_vertices - 1):
            distance[u][u + 1] = 1
            distance[u + 1][u] = 1
        distance[x][y] = 1
        distance[y][x] = 1

        # 应用Floyd-Warshall算法
        for k in range(1, num_vertices):
            for i in range(1, num_vertices):
                for j in range(1, num_vertices):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        c = Counter([distance[ii][jj] for ii in range(1, num_vertices) for jj in range(ii)])
        return [2 * c.get(ii, 0) for ii in range(1, n + 1)]
        
        
        