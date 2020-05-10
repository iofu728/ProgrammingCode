# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-10 11:03:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-10 12:27:36

"""
5407. 切披萨的方案数 显示英文描述 
通过的用户数170
尝试过的用户数252
用户总通过次数176
用户总提交次数408
题目难度Hard
给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。

切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。

请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。

示例 1：

输入：pizza = ["A..","AAA","..."], k = 3
输出：3 
解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
示例 2：

输入：pizza = ["A..","AA.","..."], k = 3
输出：1
示例 3：

输入：pizza = ["A..","A..","..."], k = 1
输出：1

提示：

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza 只包含字符 'A' 和 '.' 。
"""
import itertools
import functools


class Solution:
    MOD = 10 ** 9 + 7

    def ways(self, pizza: List[str], k: int) -> int:
        N, M = len(pizza), len(pizza[0])
        p2 = [[0] * M for _ in range(N)]
        for i, j in itertools.product(range(N), range(M)):
            p2[i][j] = 1 if pizza[i][j] == "A" else 0
        co = [[0] * (M + 1) for _ in range(N + 1)]
        for i, j in itertools.product(range(N), range(M)):
            co[i + 1][j + 1] = p2[i][j] + co[i + 1][j] + co[i][j + 1] - co[i][j]

        def f(i2, j2, i1, j1):
            return co[i2][j2] - co[i2][j1] - co[i1][j2] + co[i1][j1]

        print(co)

        @functools.lru_cache(None)
        def dfs(i, j, c):
            if c == 1:
                return 1 if f(N, M, i, j) > 0 else 0
            ans = 0
            for row in range(i + 1, N):
                if f(row, M, i, j) > 0:
                    ans += dfs(row, j, c - 1)
            for col in range(j + 1, M):
                if f(N, col, i, j) > 0:
                    ans += dfs(i, col, c - 1)
            return ans

        return dfs(0, 0, k) % self.MOD


class Solution:
    MOD = 10 ** 9 + 7

    def ways(self, pizza: List[str], k: int) -> int:
        self.res = 0

        def check(p: List[str]):
            return "".join(["".join(ii) for ii in p]).count("A")

        def one(p: List[str], idx: int):
            a, b = p[: idx + 1], p[idx + 1 :]
            if not check(a):
                return None, 0
            tt = check(b)
            if not tt:
                return None, 0
            return b, tt

        def two(p: List[str], idx: int):
            a, b = [ii[: idx + 1] for ii in p], [ii[idx + 1 :] for ii in p]
            if not check(a):
                return None, 0
            tt = check(b)
            if not tt:
                return None, 0
            return b, tt

        def dfs(p, tt):
            # print(111, p, tt)
            if tt == k - 1:
                self.res += 1
                return
            N, M = len(p), len(p[0])
            idx = 0
            while idx < N and "".join(p[idx]).count("A") == 0:
                idx += 1
            # print(p, idx)
            for ii in range(idx, N):
                a, b = one(p, ii)
                # print(ii, p, tt, a, b)
                if a is not None and b >= (k - tt - 1):
                    dfs(a, tt + 1)
                elif a is None:
                    break
            idx = 0
            while idx < M and "".join([ii[idx] for ii in p]).count("A") == 0:
                idx += 1
            for ii in range(idx, M):
                # print(ii + 100, p, tt, a, b)
                a, b = two(p, ii)
                if a is not None and b >= (k - tt - 1):
                    dfs(a, tt + 1)
                elif a is None:
                    break

        dfs(pizza, 0)
        return self.res % self.MOD
