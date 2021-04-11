# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-11 12:03:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-11 12:03:43

"""
5729. 求出 MK 平均值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。

MK 平均值 按照如下步骤计算：

如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
从这个容器中删除最小的 k 个数和最大的 k 个数。
计算剩余元素的平均值，并 取整到最近的整数 。
请你实现 MKAverage 类：

MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
void addElement(int num) 往数据流中插入一个新的元素 num 。
int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 取整到最近的整数 。
 

示例 1：

输入：
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
输出：
[null, null, null, -1, null, 3, null, null, null, 5]

解释：
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // 当前元素为 [3]
obj.addElement(1);        // 当前元素为 [3,1]
obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       // 当前元素为 [3,1,10]
obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
                          // 删除最小以及最大的 1 个元素后，容器为 [3]
                          // [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        // 当前元素为 [3,1,10,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
                          // 删除最小以及最大的 1 个元素后，容器为 [5]
                          // [5] 的平均值等于 5/1 = 5 ，故返回 5
 

提示：

3 <= m <= 105
1 <= k*2 < m
1 <= num <= 105
addElement 与 calculateMKAverage 总操作次数不超过 105 次。
"""
import bisect


class MKAverage:
    def __init__(self, m: int, k: int):
        self.c_num = 0
        self.c_sum = 0
        self.sorted = []
        self.history = []
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.c_sum += num
        self.c_num += 1
        bisect.insort(self.sorted, num)
        self.history.append(num)
        if len(self.sorted) > self.m:
            idx = bisect.bisect_left(self.sorted, self.history[-1 * self.m - 1])
            self.sorted.pop(idx)
        # print(self.sorted)

    def calculateMKAverage(self) -> int:
        if self.c_num < self.m:
            return -1
        mean = sum(self.sorted[self.k : -self.k]) / (self.m - 2 * self.k)
        return int(mean)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()