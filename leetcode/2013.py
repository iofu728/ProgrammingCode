# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-26 20:39:18
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-26 20:39:34

"""
2013. 检测正方形
给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：

添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。

实现 DetectSquares 类：

DetectSquares() 使用空数据结构初始化对象
void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
 

示例：


输入：
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
输出：
[null, null, null, null, 1, 0, null, 2]

解释：
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // 返回 1 。你可以选择：
                               //   - 第一个，第二个，和第三个点
detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
detectSquares.add([11, 2]);    // 允许添加重复的点。
detectSquares.count([11, 10]); // 返回 2 。你可以选择：
                               //   - 第一个，第二个，和第三个点
                               //   - 第一个，第三个，和第四个点
 

提示：

point.length == 2
0 <= x, y <= 1000
调用 add 和 count 的 总次数 最多为 5000
通过次数13,586提交次数25,687
"""
class DetectSquares:
    def __init__(self):
        self.x = defaultdict(set)
        self.y = defaultdict(set)
        self.c = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x[x].add(y)
        self.y[y].add(x)
        self.c[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        def union(a, b):
            return a - (a - b)
        x1, y1 = point
        res = 0
        for x2 in self.y[y1]:
            if x1 == x2:
                continue
            c1 = self.c[(x2, y1)]
            x = abs(x2 - x1)
            for y2 in [x + y1, y1 - x]:
                if y2 in self.x[x1] and y2 in self.x[x2]:
                    res += c1 * self.c[(x1, y2)] * self.c[(x2, y2)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)