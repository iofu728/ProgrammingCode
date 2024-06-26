# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-19 11:38:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-19 11:38:57

"""
100298. 到达第 K 级台阶的方案数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
给你有一个 非负 整数 k 。有一个无限长度的台阶，最低 一层编号为 0 。

虎老师有一个整数 jump ，一开始值为 0 。虎老师从台阶 1 开始，虎老师可以使用 任意 次操作，目标是到达第 k 级台阶。假设虎老师位于台阶 i ，一次 操作 中，虎老师可以：

向下走一级到 i - 1 ，但该操作 不能 连续使用，如果在台阶第 0 级也不能使用。
向上走到台阶 i + 2jump 处，然后 jump 变为 jump + 1 。
请你返回虎老师到达台阶 k 处的总方案数。

注意 ，虎老师可能到达台阶 k 处后，通过一些操作重新回到台阶 k 处，这视为不同的方案。

 

示例 1：

输入：k = 0

输出：2

解释：

2 种到达台阶 0 的方案为：

虎老师从台阶 1 开始。
执行第一种操作，从台阶 1 向下走到台阶 0 。
虎老师从台阶 1 开始。
执行第一种操作，从台阶 1 向下走到台阶 0 。
执行第二种操作，向上走 20 级台阶到台阶 1 。
执行第一种操作，从台阶 1 向下走到台阶 0 。
示例 2：

输入：k = 1

输出：4

解释：

4 种到达台阶 1 的方案为：

虎老师从台阶 1 开始，已经到达台阶 1 。
虎老师从台阶 1 开始。
执行第一种操作，从台阶 1 向下走到台阶 0 。
执行第二种操作，向上走 20 级台阶到台阶 1 。
虎老师从台阶 1 开始。
执行第二种操作，向上走 20 级台阶到台阶 2 。
执行第一种操作，向下走 1 级台阶到台阶 1 。
虎老师从台阶 1 开始。
执行第一种操作，从台阶 1 向下走到台阶 0 。
执行第二种操作，向上走 20 级台阶到台阶 1 。
执行第一种操作，向下走 1 级台阶到台阶 0 。
执行第二种操作，向上走 21 级台阶到台阶 2 。
执行第一种操作，向下走 1 级台阶到台阶 1 。
 

提示：

0 <= k <= 109
"""
class Solution:
    def waysToReachStair(self, k: int) -> int:
        if k == 0:
            return 2
        if k == 1:
            return 4
        k -= 1
        a = int(math.log2(k))
        b = 2 ** (a + 1) - 1 - k
        res = math.comb(a + 2, b)
        aa, bb = a, b
        pre = 2 ** aa
        # print(a, b, res)
        while True:
            aa += 1
            pre = pre * 2
            bb += pre
            # print(aa, bb)
            if aa + 2 < bb:
                break
            res += math.comb(aa + 2, bb)
        return res
