# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-08-28 11:07:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-08-28 11:07:40

"""
6163. 给定条件下构造矩阵 显示英文描述 
通过的用户数8
尝试过的用户数10
用户总通过次数8
用户总提交次数11
题目难度Hard
给你一个 正 整数 k ，同时给你：

一个大小为 n 的二维整数数组 rowConditions ，其中 rowConditions[i] = [abovei, belowi] 和
一个大小为 m 的二维整数数组 colConditions ，其中 colConditions[i] = [lefti, righti] 。
两个数组里的整数都是 1 到 k 之间的数字。

你需要构造一个 k x k 的矩阵，1 到 k 每个数字需要 恰好出现一次 。剩余的数字都是 0 。

矩阵还需要满足以下条件：

对于所有 0 到 n - 1 之间的下标 i ，数字 abovei 所在的 行 必须在数字 belowi 所在行的上面。
对于所有 0 到 m - 1 之间的下标 i ，数字 lefti 所在的 列 必须在数字 righti 所在列的左边。
返回满足上述要求的 任意 矩阵。如果不存在答案，返回一个空的矩阵。

 

示例 1：



输入：k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
输出：[[3,0,0],[0,0,1],[0,2,0]]
解释：上图为一个符合所有条件的矩阵。
行要求如下：
- 数字 1 在第 1 行，数字 2 在第 2 行，1 在 2 的上面。
- 数字 3 在第 0 行，数字 2 在第 2 行，3 在 2 的上面。
列要求如下：
- 数字 2 在第 1 列，数字 1 在第 2 列，2 在 1 的左边。
- 数字 3 在第 0 列，数字 2 在第 1 列，3 在 2 的左边。
注意，可能有多种正确的答案。
示例 2：

输入：k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
输出：[]
解释：由前两个条件可以得到 3 在 1 的下面，但第三个条件是 3 在 1 的上面。
没有符合条件的矩阵存在，所以我们返回空矩阵。
 

提示：

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 104
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
"""
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def findOrder(C, P):
            edges, indeg = defaultdict(list), [0] * C
            for ii, jj in P:
                edges[jj].append(ii)
                indeg[ii - 1] += 1
            q = deque([ii for ii in range(1, C + 1) if not indeg[ii - 1]])
            res = []

            while len(q):
                head = q.popleft()
                res.append(head)
                for ii in edges[head]:
                    indeg[ii - 1] -= 1
                    if indeg[ii - 1] == 0:
                        q.append(ii)
            if len(res) != C:
                res = []
            return res[::-1]
                
        x = findOrder(k, rowConditions)
        y = findOrder(k, colConditions)
        # print(x, y)
        if not x or not y:
            return []
        x_idx = {jj: ii for ii, jj in enumerate(x)}
        y_idx = {jj: ii for ii, jj in enumerate(y)}
        res = [[0] * k for ii in range(k)]
        for ii in range(1, k + 1):
            xx, yy = x_idx[ii], y_idx[ii]
            res[xx][yy] = ii
        return res
        