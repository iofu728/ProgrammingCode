# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-11-01 11:49:08
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-11-01 12:37:48

"""
5600. 第 K 条最小指令 显示英文描述 
通过的用户数283
尝试过的用户数597
用户总通过次数295
用户总提交次数930
题目难度Hard
Bob 站在单元格 (0, 0) ，想要前往目的地 destination ：(row, column) 。他只能向 右 或向 下 走。你可以为 Bob 提供导航 指令 来帮助他到达目的地 destination 。

指令 用字符串表示，其中每个字符：

'H' ，意味着水平向右移动
'V' ，意味着竖直向下移动
能够为 Bob 导航到目的地 destination 的指令可以有多种，例如，如果目的地 destination 是 (2, 3)，"HHHVV" 和 "HVHVH" 都是有效 指令 。

然而，Bob 很挑剔。因为他的幸运数字是 k，他想要遵循 按字典序排列后的第 k 条最小指令 的导航前往目的地 destination 。k  的编号 从 1 开始 。

给你一个整数数组 destination 和一个整数 k ，请你返回可以为 Bob 提供前往目的地 destination 导航的 按字典序排列后的第 k 条最小指令 。

 

示例 1：



输入：destination = [2,3], k = 1
输出："HHHVV"
解释：能前往 (2, 3) 的所有导航指令 按字典序排列后 如下所示：
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
示例 2：



输入：destination = [2,3], k = 2
输出："HHVHV"
示例 3：



输入：destination = [2,3], k = 3
输出："HHVVH"
 

提示：

destination.length == 2
1 <= row, column <= 15
1 <= k <= nCr(row + column, row)，其中 nCr(a, b) 表示组合数，即从 a 个物品中选 b 个物品的不同方案数。
"""


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        N = destination[0]
        dp, num = list(range(sum(destination) - 1, destination[1] - 1, -1)), 1
        queue = [dp]
        while queue and num < k:
            tmp = queue.pop(0)
            idx = 0
            while idx < N:
                if idx == N - 1:
                    if tmp[idx] > 0:
                        tmp[idx] -= 1
                        queue.append(tmp.copy())
                        num += 1
                        tmp[idx] += 1
                else:
                    if tmp[idx] > tmp[idx + 1] + 1:
                        tmp[idx] -= 1
                        queue.append(tmp.copy())
                        num += 1
                        tmp[idx] += 1
                idx += 1
                if num == k:
                    break
        dp = queue.pop()
        res = ["H"] * sum(destination)
        for ii in dp:
            res[ii] = "V"
        return "".join(res)


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        ans = list()
        for _ in range(h + v):
            if h > 0:
                check = math.comb(h + v - 1, h - 1)
                if k > check:
                    k -= check
                    ans.append("V")
                    v -= 1
                else:
                    ans.append("H")
                    h -= 1
            else:
                ans.append("V")
                v -= 1
        return "".join(ans)
