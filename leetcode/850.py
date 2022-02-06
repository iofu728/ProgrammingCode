# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-02 13:08:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-02 13:50:52

"""
850. 矩形面积 II
我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角 的坐标。

计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。

返回 总面积 。因为答案可能太大，返回 109 + 7 的 模 。

 

示例 1：



输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
输出：6
解释：如图所示，三个矩形覆盖了总面积为6的区域。
从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
从(1,0)到(2,3)，三个矩形都重叠。
示例 2：

输入：rectangles = [[0,0,1000000000,1000000000]]
输出：49
解释：答案是 1018 对 (109 + 7) 取模的结果， 即 49 。
 

提示：

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= xi1, yi1, xi2, yi2 <= 109
矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。
通过次数2,737提交次数6,083
"""
from sortedcontainers import SortedList


class Solution:
    MOD = 10 ** 9 + 7

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def dfs():
            res, pre = 0, -1
            for ii, jj in ps:
                res += max(0, jj - max(pre, ii))
                pre = max(pre, jj)
            return res

        line = []
        for x1, y1, x2, y2 in rectangles:
            line.append((y1, 0, x1, x2))
            line.append((y2, 1, x1, x2))
        ps, ans, pre_y = SortedList(), 0, -1
        for y, state, x1, x2 in sorted(line):
            if pre_y >= 0:
                ans += dfs() * (y - pre_y)
                ans = ans % self.MOD
            pre_y = y
            if state == 0:
                ps.add((x1, x2))
            else:
                ps.remove((x1, x2))
        return ans
