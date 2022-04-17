# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-17 11:48:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-17 11:48:51

"""
6073. 相邻字符不同的最长路径 显示英文描述 
通过的用户数66
尝试过的用户数81
用户总通过次数68
用户总提交次数115
题目难度Hard
给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。

另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。

请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。

 

示例 1：



输入：parent = [-1,0,0,1,1,2], s = "abacbe"
输出：3
解释：任意一对相邻节点字符都不同的最长路径是：0 -> 1 -> 3 。该路径的长度是 3 ，所以返回 3 。
可以证明不存在满足上述条件且比 3 更长的路径。 
示例 2：



输入：parent = [-1,0,0,0], s = "aabc"
输出：3
解释：任意一对相邻节点字符都不同的最长路径是：2 -> 0 -> 3 。该路径的长度为 3 ，所以返回 3 。
 

提示：

n == parent.length == s.length
1 <= n <= 105
对所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立
parent[0] == -1
parent 表示一棵有效的树
s 仅由小写英文字母组成
"""
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(h):
            if len(q[h]) == 0:
                return 1
            c = [dfs(ii) for ii in q[h]]
            # print(h, c)
            if len(c) >= 2:
                self.res = max(self.res, sum(nlargest(2, c)) + 1)
            else:
                self.res = max(self.res, max(c) + 1)
            return max(c) + 1
            
            
        
        g, q, p = defaultdict(set), defaultdict(set), defaultdict(int)
        root = -1
        for ii, jj in enumerate(parent):
            if jj == -1:
                root = ii
            else:
                g[jj].add(ii)
        for ii, j in g.items():
            for jj in j:
                if s[ii] != s[jj]:
                    q[ii].add(jj)
                    p[jj] += 1
        # print(p)
        self.res = 1
        for ii in range(len(parent)):
            if p[ii] == 0:
                dfs(ii)
        return self.res
        