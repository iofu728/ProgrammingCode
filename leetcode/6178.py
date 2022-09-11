# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-09-11 12:44:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-09-11 12:44:33

"""
6178. 将区间分为最少组数 显示英文描述 
通过的用户数1
尝试过的用户数4
用户总通过次数1
用户总提交次数4
题目难度Medium
给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示 闭 区间 [lefti, righti] 。

你需要将 intervals 划分为一个或者多个区间 组 ，每个区间 只 属于一个组，且同一个组中任意两个区间 不相交 。

请你返回 最少 需要划分成多少个组。

如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交 的。比方说区间 [1, 5] 和 [5, 8] 相交。

 

示例 1：

输入：intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
输出：3
解释：我们可以将区间划分为如下的区间组：
- 第 1 组：[1, 5] ，[6, 8] 。
- 第 2 组：[2, 3] ，[5, 10] 。
- 第 3 组：[1, 10] 。
可以证明无法将区间划分为少于 3 个组。
示例 2：

输入：intervals = [[1,3],[5,6],[8,10],[11,13]]
输出：1
解释：所有区间互不相交，所以我们可以把它们全部放在一个组内。
 

提示：

1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106
"""
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals = sorted(intervals, key=lambda i:(i[0], -i[1]))
        q, free = [], []
        res, l, r = 0, -1, -1
        for l, r in intervals:
            if q:
                b, a, c = heapq.heappop(q)
                while b < l:
                    free.append(c)
                    if q:
                        b, a, c = heapq.heappop(q)
                    else:
                        break
                if b >= l:
                    heapq.heappush(q, (b, a, c))
            if free:
                c = free.pop()
            else:
                res += 1
                c = res
            heapq.heappush(q, (r, l, c))
        return res
            
                
            