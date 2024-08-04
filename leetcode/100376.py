# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-04 12:53:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-04 12:53:25

"""
100376. 新增道路查询后的最短距离 II 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Hard
给你一个整数 n 和一个二维整数数组 queries。

有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。

queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。

所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。

返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。

 

示例 1：

输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]

输出： [3, 2, 1]

解释：



新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。



新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。



新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。

示例 2：

输入： n = 4, queries = [[0, 3], [0, 2]]

输出： [1, 1]

解释：



新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。



新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。

 

提示:

3 <= n <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
查询中不存在重复的道路。
不存在两个查询都满足 i != j 且 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
"""
from sortedcontainers import SortedList

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        q = SortedList()
        now = n - 1
        for ii, jj in queries:
            idx = q.bisect_left((ii, jj))
            flag = True
            j = idx
            if idx >= 1:
                x, y = q[idx - 1]
                if x <= ii and y >= jj:
                    flag = False
                elif x == ii and y <= jj:
                    now += y - x - 1
                    q.pop(idx - 1)
                    j -= 1
            # print(j, q)
            while j < len(q):
                x, y = q[j]
                if x <= ii and y >= jj:
                    flag = False
                    break
                if ii <= x and jj >= y:
                    now += y - x - 1
                    q.pop(j)
                j += 1
            # print(now, flag, jj - ii - 1)
            if flag:
                q.add((ii, jj))
                now -= jj - ii - 1
            res.append(now)
        return res
                
        