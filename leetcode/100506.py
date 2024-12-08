# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-12-08 12:16:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-12-08 12:16:56

"""
100506. 用点构造面积最大的矩形 I 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Medium
给你一个数组 points，其中 points[i] = [xi, yi] 表示无限平面上一点的坐标。

你的任务是找出满足以下条件的矩形可能的 最大 面积：

矩形的四个顶点必须是数组中的 四个 点。
矩形的内部或边界上 不能 包含任何其他点。
矩形的边与坐标轴 平行 。
返回可以获得的 最大面积 ，如果无法形成这样的矩形，则返回 -1。

 

示例 1：

输入： points = [[1,1],[1,3],[3,1],[3,3]]

输出：4

解释：

示例 1 图示

我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。

示例 2：

输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

输出：-1

解释：

示例 2 图示

唯一一组可能构成矩形的点为 [1,1], [1,3], [3,1] 和 [3,3]，但点 [2,2] 总是位于矩形内部。因此，返回 -1 。

示例 3：

输入： points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

输出：2

解释：

示例 3 图示

点 [1,3], [1,2], [3,2], [3,3] 可以构成面积最大的矩形，面积为 2。此外，点 [1,1], [1,2], [3,1], [3,2] 也可以构成一个符合题目要求的矩形，面积相同。

 

提示：

1 <= points.length <= 10
points[i].length == 2
0 <= xi, yi <= 100
给定的所有点都是 唯一 的。
"""
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        def check(x1, x2, y1, y2):
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for i, j in points:
                if (x1 < i < x2 and y1 <= j <= y2) or (x1 <= i <= x2 and y1 < j < y2):
                    return False
            return True
        N = len(points)
        p = set([(ii, jj) for ii, jj in points])
        res = -1
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                if (x1, y2) in p and (x2, y1) in p:
                    t = abs(x2 - x1) * abs(y2 - y1)
                    if t and check(x1, x2, y1, y2):
                        res = max(res, t)
        return res
                