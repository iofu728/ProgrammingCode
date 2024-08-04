# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-04 12:51:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-04 12:52:13

"""
100388. 交替组 III 显示英文描述 
通过的用户数6
尝试过的用户数54
用户总通过次数6
用户总提交次数115
题目难度Hard
给你一个整数数组 colors 和一个二维整数数组 queries 。colors表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ：

colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。
colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。
环中连续若干块瓷砖的颜色如果是 交替 颜色（也就是说这组瓷砖中除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替组。

你需要处理两种类型的查询：

queries[i] = [1, sizei]，确定大小为sizei的 交替组 的数量。
queries[i] = [2, indexi, colori]，将colors[indexi]更改为colori。
返回数组 answer，数组中按顺序包含第一种类型查询的结果。

注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。

 

示例 1：

输入：colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]

输出：[2]

解释：

第一次查询：

将 colors[1] 改为 0。



第二次查询：

统计大小为 4 的交替组的数量：



示例 2：

输入：colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]

输出：[2,0]

解释：



第一次查询：

统计大小为 3 的交替组的数量。



第二次查询：colors不变。

第三次查询：不存在大小为 5 的交替组。

 

提示：

4 <= colors.length <= 5 * 104
0 <= colors[i] <= 1
1 <= queries.length <= 5 * 104
queries[i][0] == 1 或 queries[i][0] == 2
对于所有的i：
queries[i][0] == 1： queries[i].length == 2, 3 <= queries[i][1] <= colors.length - 1
queries[i][0] == 2： queries[i].length == 3, 0 <= queries[i][1] <= colors.length - 1, 0 <= queries[i][2] <= 1

"""
from sortedcontainers import SortedList

class Solution(object):
    def numberOfAlternatingGroups(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(colors)
        s = SortedList()
        sum = [0] * (n + 1)
        count = [0] * (n + 1)
        r = []
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                self.insert(n, i - 1, s, count, sum)
        if colors[n - 1] == colors[0]:
            self.insert(n, n - 1, s, count, sum)
        for q in queries:
            if q[0] == 1:
                k = q[1]
                r.append(n if not s else (self.getsum(n, sum) - self.getsum(k - 1, sum) - (k - 1) * (self.getsum(n, count) - self.getsum(k - 1, count))))
            else:
                ind = q[1]
                if colors[ind] == q[2]:
                    continue
                colors[ind] = q[2]
                before = (ind + n - 1) % n
                if colors[ind] == colors[before]:
                    self.insert(n, before, s, count, sum)
                else:
                    self.remove(n, before, s, count, sum)
                after = (ind + 1) % n
                if colors[ind] == colors[after]:
                    self.insert(n, ind, s, count, sum)
                else:
                    self.remove(n, ind, s, count, sum)
        return r
    def lowbit(self, x):
        return x & (-x)
    def update(self, i, x, c):
        if i == 0:
            return
        while i < len(c):
            c[i] += x
            i += self.lowbit(i)
    def getsum(self, i, c):
        r = 0
        while i:
            r += c[i]
            i -= self.lowbit(i)
        return r
    def make(self, insert, t, n, s, count, sum):
        if len(s) == 1:
            self.update(n, 1 if insert else -1, count)
            self.update(n, n if insert else -n, sum)
        before = (t - 1 + len(s)) % len(s)
        after = (t + 1) % len(s)
        len1 = n if len(s) == 2 else (s[after] - s[before] + n) % n
        self.update(len1, -1 if insert else 1, count)
        self.update(len1, -len1 if insert else len1, sum)
        len2 = (s[t] - s[before] + n) % n
        self.update(len2, 1 if insert else -1, count)
        self.update(len2, len2 if insert else -len2, sum)
        len3 = (s[after] - s[t] + n) % n
        self.update(len3, 1 if insert else -1, count)
        self.update(len3, len3 if insert else -len3, sum)
        if not insert:
            s.pop(t)
    def insert(self, n, x, s, count, sum):
        s.add(x)
        self.make(True, s.index(x), n, s, count, sum)
    def remove(self, n, x, s, count, sum):
        self.make(False, s.index(x), n, s, count, sum)
