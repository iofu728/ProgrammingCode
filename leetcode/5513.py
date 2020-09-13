# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 10:47:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 11:15:08

"""
5513. 连接所有点的最小费用 显示英文描述 
通过的用户数37
尝试过的用户数46
用户总通过次数37
用户总提交次数49
题目难度Medium
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

 

示例 1：



输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：

我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
示例 2：

输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
示例 3：

输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4
示例 4：

输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000
示例 5：

输入：points = [[0,0]]
输出：0
 

提示：

1 <= points.length <= 1000
-106 <= xi, yi <= 106
所有点 (xi, yi) 两两不同。
"""


class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        def kruskal(edge_list):
            group = {ii: ii for ii in range(N)}
            group2 = [[ii] for ii in range(N)]
            ans = 0
            for edge in edge_list:
                m = group[edge[0]]
                n = group[edge[1]]
                if m != n:
                    ans += edge[2]
                    for ii in group2[n]:
                        group[ii] = m
                    group2[m] = group2[m] + group2[n]
                    group2[n] = []
            return ans

        N = len(p)
        edge_list = []
        for ii in range(N):
            for jj in range(ii):
                edge_list.append(
                    [ii, jj, abs(p[ii][0] - p[jj][0]) + abs(p[ii][1] - p[jj][1])]
                )
        edge_list = sorted(edge_list, key=lambda i: i[-1])
        return kruskal(edge_list)

