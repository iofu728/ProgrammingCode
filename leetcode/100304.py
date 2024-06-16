# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-16 11:43:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-16 11:43:43

"""
100304. 构成整天的下标对数目 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j 且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。

整天 定义为时间持续时间是 24 小时的 整数倍 。

例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。

 

示例 1：

输入： hours = [12,12,30,24,24]

输出： 2

解释：

构成整天的下标对分别是 (0, 1) 和 (3, 4)。

示例 2：

输入： hours = [72,48,24,3]

输出： 3

解释：

构成整天的下标对分别是 (0, 1)、(0, 2) 和 (1, 2)。

 

提示：

1 <= hours.length <= 100
1 <= hours[i] <= 109
"""
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        c = defaultdict(int)
        res = 0
        for i in hours:
            now = i % 24
            res += c[(24 - now) % 24]
            c[now] += 1
        return res
            
            