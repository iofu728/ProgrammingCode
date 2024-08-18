# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-18 12:24:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-18 12:25:02

"""
100386. 超级饮料的最大强化能量 显示英文描述 
通过的用户数19
尝试过的用户数22
用户总通过次数19
用户总提交次数23
题目难度Medium
来自未来的体育科学家给你两个整数数组 energyDrinkA 和 energyDrinkB，数组长度都等于 n。这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。

你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。

返回在接下来的 n 小时内你能获得的 最大 总强化能量。

注意 你可以选择从饮用任意一种能量饮料开始。

 

示例 1：

输入：energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]

输出：5

解释：

要想获得 5 点强化能量，需要选择只饮用能量饮料 A（或者只饮用 B）。

示例 2：

输入：energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]

输出：7

解释：

第一个小时饮用能量饮料 A。
切换到能量饮料 B ，在第二个小时无法获得强化能量。
第三个小时饮用能量饮料 B ，并获得强化能量。
 

提示：

n == energyDrinkA.length == energyDrinkB.length
3 <= n <= 105
1 <= energyDrinkA[i], energyDrinkB[i] <= 105
"""
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)
        last = [0, 0]
        dp = [0, 0]
        for i in range(N):
            now = [0, 0]
            now[0] = max(dp[0] + energyDrinkA[i], last[1] + energyDrinkA[i])
            now[1] = max(dp[1] + energyDrinkB[i], last[0] + energyDrinkB[i])
            last = dp
            dp = now
        return max(dp)