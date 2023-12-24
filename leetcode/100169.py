# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-12-24 12:09:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-12-24 12:09:48

"""
100169. 移除栅栏得到的正方形田地的最大面积 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
有一个大型的 (m - 1) x (n - 1) 矩形田地，其两个对角分别是 (1, 1) 和 (m, n) ，田地内部有一些水平栅栏和垂直栅栏，分别由数组 hFences 和 vFences 给出。

水平栅栏为坐标 (hFences[i], 1) 到 (hFences[i], n)，垂直栅栏为坐标 (1, vFences[i]) 到 (m, vFences[i]) 。

返回通过 移除 一些栅栏（可能不移除）所能形成的最大面积的 正方形 田地的面积，或者如果无法形成正方形田地则返回 -1。

由于答案可能很大，所以请返回结果对 109 + 7 取余 后的值。

注意：田地外围两个水平栅栏（坐标 (1, 1) 到 (1, n) 和坐标 (m, 1) 到 (m, n) ）以及两个垂直栅栏（坐标 (1, 1) 到 (m, 1) 和坐标 (1, n) 到 (m, n) ）所包围。这些栅栏 不能 被移除。

 

示例 1：



输入：m = 4, n = 3, hFences = [2,3], vFences = [2]
输出：4
解释：移除位于 2 的水平栅栏和位于 2 的垂直栅栏将得到一个面积为 4 的正方形田地。
示例 2：



输入：m = 6, n = 7, hFences = [2], vFences = [4]
输出：-1
解释：可以证明无法通过移除栅栏形成正方形田地。
 

提示：

3 <= m, n <= 109
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences 和 vFences 中的元素是唯一的。

"""
class Solution:
    MODS = 10 ** 9 + 7
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        g = defaultdict(int)
        # g[0] = 1
        res = -1
        for ii in hFences + [1, m]:
            for jj in vFences + [1, n]:
                if ii - jj not in g:
                    g[ii - jj] = ii
                else:
                    g[ii - jj] = min(ii, g[ii - jj])
        for ii in hFences + [1, m]:
            for jj in vFences + [1, n]:
                if ii - jj not in g:
                    continue
                c = g[ii - jj]
                if c != ii:
                    res = max(ii - c, res)
        return pow(res, 2, self.MODS) if res != -1 else res