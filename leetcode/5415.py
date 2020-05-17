# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-17 10:55:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-17 11:36:34

"""
5415. 圆形靶内的最大飞镖数量 显示英文描述 
通过的用户数111
尝试过的用户数274
用户总通过次数117
用户总提交次数469
题目难度Hard
墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。

投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。

请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。

示例 1：

输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
输出：4
解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
示例 2：



输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
输出：5
解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
示例 3：

输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
输出：1
示例 4：

输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
输出：4
 

提示：

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000
"""


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        r2, N, max_res, map_t = r ** 2, len(points), 1, set()
        def get_mid(a, b):
            ax, ay = a
            bx, by = b
            lx = bx - ax
            ly = by - ay
            lxy = (lx ** 2 + ly ** 2) ** 0.5
            if (lxy / 2) ** 2 > r2:
                return (None, None), (None, None)
            l = (r2 - (lxy / 2) ** 2) ** 0.5
            yy = l * lx / lxy
            xx = l * ly / lxy
            mx = (ax + bx) / 2
            my = (ay + by) / 2
            return (mx + xx, my - yy), (mx - xx, my + yy)
        def is_in(rx, ry, x, y):
            lx = rx - x
            ly = ry - y
            # print(x, y, lx ** 2 + ly ** 2 - r2)
            return lx ** 2 + ly ** 2 <= r2 + 0.01
        def count_in(rx, ry):
            return len([1 for ii in points if is_in(rx, ry, ii[0], ii[1])])
        for ii in range(N):
            for jj in range(ii + 1, N):
                (rx1, ry1), (rx2, ry2) = get_mid(points[ii], points[jj])
                # print(rx1, ry1, rx2, ry2)
                if rx1 is None:
                    continue
                if (rx1, ry1) not in map_t:
                    c1 = count_in(rx1, ry1)
                else:
                    c1 = 0
                if (rx2, ry2) not in map_t:
                    c2 = count_in(rx2, ry2)
                else:
                    c2 = 0
                map_t.add((rx1, ry1))
                map_t.add((rx2, ry2))
                max_res = max(c1, c2, max_res)
        return max_res
                
        
        