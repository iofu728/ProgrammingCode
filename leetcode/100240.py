"""
100240. 最小化曼哈顿距离 显示英文描述 
通过的用户数6
尝试过的用户数11
用户总通过次数6
用户总提交次数12
题目难度Hard
给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。

两点之间的距离定义为它们的曼哈顿距离。

请你恰好移除一个点，返回移除后任意两点之间的 最大 距离可能的 最小 值。

 

示例 1：

输入：points = [[3,10],[5,15],[10,2],[4,4]]
输出：12
解释：移除每个点后的最大距离如下所示：
- 移除第 0 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间，为 |5 - 10| + |15 - 2| = 18 。
- 移除第 1 个点后，最大距离在点 (3, 10) 和 (10, 2) 之间，为 |3 - 10| + |10 - 2| = 15 。
- 移除第 2 个点后，最大距离在点 (5, 15) 和 (4, 4) 之间，为 |5 - 4| + |15 - 4| = 12 。
- 移除第 3 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间的，为 |5 - 10| + |15 - 2| = 18 。
在恰好移除一个点后，任意两点之间的最大距离可能的最小值是 12 。
示例 2：

输入：points = [[1,1],[1,1],[1,1]]
输出：0
解释：移除任一点后，任意两点之间的最大距离都是 0 。
 

提示：

3 <= points.length <= 105
points[i].length == 2
1 <= points[i][0], points[i][1] <= 108
"""
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def get_x(a, b, z):
            r1, r2 = [], []
            for idx, (x, y) in enumerate(points):
                if z is not None and z == idx:
                    continue
                score = x * a + b * y
                if len(r1) == 0:
                    r1 = [x, y]
                elif len(r2) == 0:
                    r2 = [x, y]
                    if r1[0] * a + r1[1] * b < score:
                        r1, r2 = r2, r1
                elif r1[0] * a + r1[1] * b < score:
                    r2 = r1
                    r1 = [x, y]
                elif r2[0] * a + r2[1] * b < score:
                    r2 = [x, y]
            return r1, r2
        
        if len(points) <= 100:
            res = float("inf")
            for idx, (x, y) in enumerate(points):
                a1, a2 = get_x(-1, 1, idx)
                b1, b2 = get_x(1, -1, idx)
                c1, c2 = get_x(1, 1, idx)
                d1, d2 = get_x(-1, -1, idx)
                score = max(abs(a1[0] - b1[0]) + abs(a1[1] - b1[1]), abs(c1[0] - d1[0]) + abs(c1[1] - d1[1]))
                res = min(res, score)
            return res
     
        a1, a2 = get_x(-1, 1, None)
        b1, b2 = get_x(1, -1, None)
        c1, c2 = get_x(1, 1, None)
        d1, d2 = get_x(-1, -1, None)
        # print(a1, a2, b1, b2, c1, c2, d1, d2)
        res = float("inf")
        for a, b, c, d in [(a1, b2, c1, d1), (a2, b1, c1, d1), (c1, d2, a1, b1), (c2, d1, a1, b1)]:
            score = max(abs(a[0] - b[0]) + abs(a[1] - b[1]), abs(c[0] - d[0]) + abs(c[1] - d[1]))
            res = min(res, score)
        return res
            