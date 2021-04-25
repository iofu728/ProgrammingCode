# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-25 11:06:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-25 11:52:15
"""
5741. 最高建筑高度 显示英文描述 
通过的用户数20
尝试过的用户数41
用户总通过次数23
用户总提交次数56
题目难度Hard
在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。

这座城市对这些新建筑有一些规定：

每栋建筑的高度必须是一个非负整数。
第一栋建筑的高度 必须 是 0 。
任意两栋相邻建筑的高度差 不能超过  1 。
除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [idi, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。

题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。

请你返回 最高 建筑能达到的 最高高度 。

 

示例 1：


输入：n = 5, restrictions = [[2,1],[4,1]]
输出：2
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。
示例 2：


输入：n = 6, restrictions = []
输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。
示例 3：


输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。
 

提示：

2 <= n <= 109
0 <= restrictions.length <= min(n - 1, 105)
2 <= idi <= n
idi 是 唯一的 。
0 <= maxHeighti <= 109
"""


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        res = 0
        r_map = [[ii, jj] for ii, jj in restrictions if jj < ii - 1]
        r_map = sorted(r_map, key=lambda i: i)
        N = len(r_map)
        for kk, (ii, jj) in sorted(enumerate(r_map), key=lambda i: i[1][1] - i[1][0]):
            _, j = r_map[kk]
            j = min(j, jj)
            r_map[kk] = [ii, j]
            k = kk - 1
            while k >= 0:
                tmp_i, tmp_j = r_map[k]
                if j + (ii - tmp_i) < tmp_j:
                    r_map[k] = [tmp_i, j + (ii - tmp_i)]
                else:
                    break
                k -= 1
            k = kk + 1
            while k < N:
                tmp_i, tmp_j = r_map[k]
                if j + (-ii + tmp_i) < tmp_j:
                    r_map[k] = [tmp_i, j + (-ii + tmp_i)]
                else:
                    break
                k += 1
        pre_i, pre_h = 1, 0
        res = 0
        for ii, jj in r_map:
            xx = abs(ii - pre_i)
            yy = abs(jj - pre_h)
            have = max(jj, pre_h) + abs(xx - yy) // 2
            res = max(res, have)
            pre_i, pre_h = ii, jj
        xx = n - pre_i
        res = max(res, pre_h + xx)
        return res
