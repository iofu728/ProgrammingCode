# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-10 14:03:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-10 14:03:44

"""
6112. 装满杯子需要的最短总时长 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。

给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。

 

示例 1：

输入：amount = [1,4,2]
输出：4
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。
示例 2：

输入：amount = [5,4,4]
输出：7
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。
示例 3：

输入：amount = [5,0,0]
输出：5
解释：每秒装满一杯冷水。
 

提示：

amount.length == 3
0 <= amount[i] <= 100
"""


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        d = []
        for ii in amount:
            if ii > 0:
                heapq.heappush(d, -ii)
        res = 0
        while d:
            a = heapq.heappop(d)
            if d:
                b = heapq.heappop(d)
                if b + 1 != 0:
                    heapq.heappush(d, b + 1)

            if a + 1 != 0:
                heapq.heappush(d, a + 1)
            res += 1
        return res
