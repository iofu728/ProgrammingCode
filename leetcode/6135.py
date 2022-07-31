"""
6135. 图中的最长环 显示英文描述 
通过的用户数594
尝试过的用户数902
用户总通过次数635
用户总提交次数1613
题目难度Hard
给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。

图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么 edges[i] == -1 。

请你返回图中的 最长 环，如果没有任何环，请返回 -1 。

一个环指的是起点和终点是 同一个 节点的路径。

 

示例 1：



输入：edges = [3,3,4,2,3]
输出去：3
解释：图中的最长环是：2 -> 4 -> 3 -> 2 。
这个环的长度为 3 ，所以返回 3 。
示例 2：



输入：edges = [2,-1,3,1]
输出：-1
解释：图中没有任何环。
 

提示：

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
"""


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        d = [0] * N
        ans = -1
        for a in range(N):
            b = a
            # print(a)
            if d[a]:
                continue
            res = 1
            d[a] = 1
            while a != -1:
                a = edges[a]
                res += 1
                # print(a, res)
                if a != -1 and d[a]:
                    ans = max(ans, res - d[a])
                    break
                if a != -1:
                    d[a] = res
            if a == -1:
                a = b
                d[a] = 0
                while a != -1:
                    a = edges[a]
                    if a != -1:
                        d[a] = 0

        return ans
