# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-05-14 10:59:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-05-14 10:59:17

"""
6432. 统计完全连通分量的数量 显示英文描述 
通过的用户数25
尝试过的用户数26
用户总通过次数25
用户总提交次数28
题目难度Medium
给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。给你一个二维整数数组 edges 其中 edges[i] = [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。

返回图中 完全连通分量 的数量。

如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。

如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。

 

示例 1：



输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
输出：3
解释：如上图所示，可以看到此图所有分量都是完全连通分量。
示例 2：



输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
输出：1
解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
因此，在图中完全连接分量的数量是 1 。
 

提示：

1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
不存在重复的边
"""
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def getroot(r, p):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while q != p:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
        ra = list(range(n))
        done = set()
        for x, y in edges:
            a, b = getroot(ra, x), getroot(ra, y)
            ra[b] = a
            done.add(tuple(sorted([x, y])))
        
        g = defaultdict(set)
        for ii in range(n):
            fa = getroot(ra, ii)
            g[fa].add(ii)
        res = 0
        # print(g, done)
        for fa, sons in g.items():
            M = len(sons)
            sons = sorted(sons)
            flag = True
            for ii in range(M):
                for jj in range(ii + 1, M):
                    x, y = sons[ii], sons[jj]
                    # print(x, y)
                    if (x, y) not in done:
                        flag = False
                        break
                if flag is False:
                    break
            if flag is True:
                res += 1
        return res