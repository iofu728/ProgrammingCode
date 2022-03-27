# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-27 11:13:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-27 11:14:14

"""
5269. 从栈中取出 K 个硬币的最大面值和 显示英文描述 
通过的用户数6
尝试过的用户数8
用户总通过次数6
用户总提交次数13
题目难度Hard
一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币。

每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里。

给你一个列表 piles ，其中 piles[i] 是一个整数数组，分别表示第 i 个栈里 从顶到底 的硬币面值。同时给你一个正整数 k ，请你返回在 恰好 进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少 。

 

示例 1：



输入：piles = [[1,100,3],[7,8,9]], k = 2
输出：101
解释：
上图展示了几种选择 k 个硬币的不同方法。
我们可以得到的最大面值为 101 。
示例 2：

输入：piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
输出：706
解释：
如果我们所有硬币都从最后一个栈中取，可以得到最大面值和。
 

提示：

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 105
1 <= k <= sum(piles[i].length) <= 2000
"""
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(x, y):
            if x >= N:
                return 0
            res = dp(x + 1, y)
            pre = 0
            for ii in range(min(len(piles[x]), y)):
                pre += piles[x][ii]
                res = max(res, pre + dp(x + 1, y - ii - 1))
            return res
            
        N = len(piles)
        return dp(0, k)