# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-05-21 12:21:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-05-21 12:21:10

"""
6441. 求一个整数的惩罚数 显示英文描述 
通过的用户数1
尝试过的用户数1
用户总通过次数1
用户总提交次数1
题目难度Medium
给你一个正整数 n ，请你返回 n 的 惩罚数 。

n 的 惩罚数 定义为所有满足以下条件 i 的数的平方和：

1 <= i <= n
i * i 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 i 。
 

示例 1：

输入：n = 10
输出：182
解释：总共有 3 个整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
因此，10 的惩罚数为 1 + 81 + 100 = 182
示例 2：

输入：n = 37
输出：1478
解释：总共有 4 个整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
- 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。
因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478
 

提示：

1 <= n <= 1000
"""
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_ok(y):
            s = str(y ** 2)
            if sum([int(ii) for ii in s]) > y:
                return False
            if sum([int(ii) for ii in s]) == y:
                return True
            return dfs(s, y)
        def dfs(ss, t):
            # print(ss, t)
            if t < 0:
                return False
            if len(ss) == 0:
                return t == 0
            res = False
            if ss[0] == "0":
                res = dfs(ss[1:], t)
            else:
                for ii in range(1, len(ss) + 1):
                    if dfs(ss[ii:], t - int(ss[:ii])) is True:
                        return True
            return res
        res = 0
        for ii in range(1, n + 1):
            if is_ok(ii):
                # print(ii)
                res += ii ** 2
        return res
                
            