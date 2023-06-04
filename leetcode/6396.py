# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-04 14:19:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-04 14:20:04

"""
6396. 统计整数数目 显示英文描述 
通过的用户数31
尝试过的用户数53
用户总通过次数32
用户总提交次数76
题目难度Hard
给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.
请你返回好整数的数目。答案可能很大，请返回答案对 109 + 7 取余后的结果。

注意，digit_sum(x) 表示 x 各位数字之和。

 

示例 1：

输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
输出：11
解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。
示例 2：

输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
输出：5
解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
 

提示：

1 <= num1 <= num2 <= 1022
1 <= min_sum <= max_sum <= 400
"""
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def solve(num):
            n = len(num)
            dp = [[[0] * 2 for _ in range(max_sum + 1)] for _ in range(n + 1)]
            # dp[i][j][k] 表示当前考虑到第 i 位，数位和为 j，是否存在上界限制的方案数
            dp[0][0][1] = 1
            for i in range(1, n + 1):
                for j in range(max_sum + 1):
                    for k in range(10):
                        if j - k < 0: break
                        if k < int(num[i - 1]):
                            dp[i][j][0] += dp[i - 1][j - k][0] + dp[i - 1][j - k][1]
                        elif k == int(num[i - 1]):
                            dp[i][j][0] += dp[i - 1][j - k][0]
                            dp[i][j][1] += dp[i - 1][j - k][1]
                        else:
                            dp[i][j][0] += dp[i - 1][j - k][0]
            ans = 0
            for i in range(min_sum, max_sum + 1):
                ans += dp[n][i][0] + dp[n][i][1]
            return ans
        return (solve(num2) - solve(str(int(num1) - 1))) % (10 ** 9 + 7)