# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-25 20:09:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-25 20:09:24

"""
1857. 有向图中最大颜色值
给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。

给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。同时给你一个二维数组 edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。

图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1 在图中有一条有向边。路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。

请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。

 

示例 1：



输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
输出：3
解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。
示例 2：



输入：colors = "a", edges = [[0,0]]
输出：-1
解释：从 0 到 0 有一个环。
 

提示：

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors 只含有小写英文字母。
0 <= aj, bj < n
通过次数2,451提交次数5,342
"""
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        g, gg = defaultdict(list), defaultdict(int)
        for ii, jj in edges:
            g[ii].append(jj)
            gg[jj] += 1
        queue = [ii for ii in range(N) if gg[ii] == 0]
        f = [[0] * 26 for _ in range(N)]
        times = 0
        while queue:
            times += 1
            head = queue.pop(0)
            f[head][ord(colors[head]) - ord("a")] += 1
            for ii in g[head]:
                gg[ii] -= 1
                for jj in range(26):
                    f[ii][jj] = max(f[ii][jj], f[head][jj])
                if gg[ii] == 0:
                    queue.append(ii)
        if times != N:
            return -1
        return max([max(ii) for ii in f])
