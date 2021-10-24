# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-24 11:59:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-24 11:59:25

"""
5908. 统计最高分的节点数目 显示英文描述 
通过的用户数38
尝试过的用户数41
用户总通过次数38
用户总提交次数64
题目难度Medium
给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。

一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。

请你返回有 最高得分 节点的 数目 。

 

示例 1:

example-1

输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
示例 2：

example-2

输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
 

提示：

n == parents.length
2 <= n <= 105
parents[0] == -1
对于 i != 0 ，有 0 <= parents[i] <= n - 1
parents 表示一棵二叉树。
"""


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        total, root, N = 0, 0, len(parents)
        g = defaultdict(list)
        for ii, jj in enumerate(parents):
            if jj != -1:
                g[jj].append(ii)
        num = [[]] * N

        def dfs(now):
            res = []
            for ii in g[now]:
                res.append(sum(dfs(ii)) + 1)
            if len(res) < 2:
                res += [0] * (2 - len(res))
            num[now] = res
            return res

        dfs(0)
        total = sum(num[0]) + 1
        res, k = 0, 0
        for ii, jj in num:
            kk = total - ii - jj - 1
            tmp = 1
            for i in [ii, jj, kk]:
                if i:
                    tmp *= i
            if tmp == res:
                k += 1
            elif tmp > res:
                res, k = tmp, 1
        return k
