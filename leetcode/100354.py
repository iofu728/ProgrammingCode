# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-11 11:32:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-11 11:32:43

"""
100354. 统计好节点的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
现有一棵 无向 树，树中包含 n 个节点，按从 0 到 n - 1 标记。树的根节点是节点 0 。给你一个长度为 n - 1 的二维整数数组 edges，其中 edges[i] = [ai, bi] 表示树中节点 ai 与节点 bi 之间存在一条边。

如果一个节点的所有子节点为根的 子树 包含的节点数相同，则认为该节点是一个 好节点。

返回给定树中 好节点 的数量。

子树 指的是一个节点以及它所有后代节点构成的一棵树。

 

 

示例 1：

输入：edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]

输出：7

说明：


树的所有节点都是好节点。

示例 2：

输入：edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]

输出：6

说明：


树中有 6 个好节点。上图中已将这些节点着色。

示例 3：

输入：edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]

输出：12

解释：


除了节点 9 以外其他所有节点都是好节点。

 

提示：

2 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
输入确保 edges 总表示一棵有效的树。
"""
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        @lru_cache(None)
        def get_x(x):
            res =  1
            for ii in g[x]:
                res += get_x(ii)
            return res
        
        @lru_cache(None)
        def is_good(x):
            if len(g[x]) == 0:
                return True
            return len(set([get_x(ii) for ii in g[x]])) == 1
        gg = defaultdict(list)
        g = defaultdict(list)
        
        for ii, jj in edges:
            gg[ii].append(jj)
            gg[jj].append(ii)
        done = set([0])
        q = [0]
        while q:
            now = q.pop(0)
            done.add(now)
            for ii in gg[now]:
                if ii not in done:
                    q.append(ii)
                    g[now].append(ii)
        return len([1 for ii in range(n) if is_good(ii)])
        
        
            
            