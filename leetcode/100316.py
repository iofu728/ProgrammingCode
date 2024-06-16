# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-16 11:44:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-16 11:44:17

"""
100316. 施咒的最大总伤害 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Medium
一个魔法师有许多不同的咒语。

给你一个数组 power ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。

已知魔法师使用伤害值为 power[i] 的咒语时，他们就 不能 使用伤害为 power[i] - 2 ，power[i] - 1 ，power[i] + 1 或者 power[i] + 2 的咒语。

每个咒语最多只能被使用 一次 。

请你返回这个魔法师可以达到的伤害值之和的 最大值 。

 

示例 1：

输入：power = [1,1,3,4]

输出：6

解释：

可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。

示例 2：

输入：power = [7,1,6,6]

输出：13

解释：

可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。

 

提示：

1 <= power.length <= 105
1 <= power[i] <= 109
"""
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        N = len(c)
        dp = [0] * 4
        last = -100
        print(sorted(c.items(), key=lambda i:(i[0])))
        for i, j in sorted(c.items(), key=lambda i:(i[0])):
            now = [0] * 4
            if i > last + 2:
                dp[-1] = max(dp)
                dp[0] = 0
                dp[1] = 0
                dp[2] = 0
            elif i == last + 2:
                dp[-1] = max(dp[1:])
                dp[2] = dp[0]
                dp[1] = 0
                dp[0] = 0
            elif i == last + 1:
                dp[-1] = max(dp[2:])
                dp[2] = dp[1]
                dp[1] = dp[0]
                dp[0] = 0
            # print(dp)
            now[0] = dp[-1] + j * i
            now[1] = dp[1]
            now[2] = dp[2]
            now[3] = dp[3]
            dp = now
            last = i
            # print(dp)
        return max(dp)