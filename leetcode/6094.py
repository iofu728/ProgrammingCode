# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-06-12 13:59:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-06-12 14:00:09

"""
6094. 公司命名 显示英文描述 
通过的用户数33
尝试过的用户数44
用户总通过次数33
用户总提交次数64
题目难度Hard
给你一个字符串数组 ideas 表示在公司命名过程中使用的名字列表。公司命名流程如下：

从 ideas 中选择 2 个 不同 名字，称为 ideaA 和 ideaB 。
交换 ideaA 和 ideaB 的首字母。
如果得到的两个新名字 都 不在 ideas 中，那么 ideaA ideaB（串联 ideaA 和 ideaB ，中间用一个空格分隔）是一个有效的公司名字。
否则，不是一个有效的名字。
返回 不同 且有效的公司名字的数目。

 

示例 1：

输入：ideas = ["coffee","donuts","time","toffee"]
输出：6
解释：下面列出一些有效的选择方案：
- ("coffee", "donuts")：对应的公司名字是 "doffee conuts" 。
- ("donuts", "coffee")：对应的公司名字是 "conuts doffee" 。
- ("donuts", "time")：对应的公司名字是 "tonuts dime" 。
- ("donuts", "toffee")：对应的公司名字是 "tonuts doffee" 。
- ("time", "donuts")：对应的公司名字是 "dime tonuts" 。
- ("toffee", "donuts")：对应的公司名字是 "doffee tonuts" 。
因此，总共有 6 个不同的公司名字。

下面列出一些无效的选择方案：
- ("coffee", "time")：在原数组中存在交换后形成的名字 "toffee" 。
- ("time", "toffee")：在原数组中存在交换后形成的两个名字。
- ("coffee", "toffee")：在原数组中存在交换后形成的两个名字。
示例 2：

输入：ideas = ["lack","back"]
输出：0
解释：不存在有效的选择方案。因此，返回 0 。
 

提示：

2 <= ideas.length <= 5 * 104
1 <= ideas[i].length <= 10
ideas[i] 由小写英文字母组成
ideas 中的所有字符串 互不相同
"""


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        N = len(ideas)
        res = 0
        g = defaultdict(set)
        c = {chr(ii + ord('a')): defaultdict(int) for ii in range(26)}
        for ii in ideas:
            g[ii[0]].add(ii)
        for ii in ideas:
            for jj in range(26):
                k = chr(jj + ord('a'))
                if k == ii[0]:
                    continue
                if k + ii[1:] not in g[k] and len(g[k]):
                    c[ii[0]][k] += 1
        res = 0
        for ii in range(26):
            x = chr(ii + ord('a'))
            for jj in range(26):
                y = chr(jj + ord('a'))
                # if c[x][y] or c[y][x]:
                #     print(x, y, c[x][y], c[y][x])
                res += c[x][y] * c[y][x]

        return res
