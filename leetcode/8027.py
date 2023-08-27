# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-27 14:29:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-27 14:29:50

"""
8027. 在传球游戏中最大化函数值 显示英文描述 
通过的用户数97
尝试过的用户数502
用户总通过次数111
用户总提交次数1241
题目难度Medium
给你一个长度为 n 下标从 0 开始的整数数组 receiver 和一个整数 k 。

总共有 n 名玩家，玩家 编号 互不相同，且为 [0, n - 1] 中的整数。这些玩家玩一个传球游戏，receiver[i] 表示编号为 i 的玩家会传球给编号为 receiver[i] 的玩家。玩家可以传球给自己，也就是说 receiver[i] 可能等于 i 。

你需要从 n 名玩家中选择一名玩家作为游戏开始时唯一手中有球的玩家，球会被传 恰好 k 次。

如果选择编号为 x 的玩家作为开始玩家，定义函数 f(x) 表示从编号为 x 的玩家开始，k 次传球内所有接触过球玩家的编号之 和 ，如果有玩家多次触球，则 累加多次 。换句话说， f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver(k)[x] 。

你的任务时选择开始玩家 x ，目的是 最大化 f(x) 。

请你返回函数的 最大值 。

注意：receiver 可能含有重复元素。

 

示例 1：

传递次数	传球者编号	接球者编号	x + 所有接球者编号
 	 	 	2
1	2	1	3
2	1	0	3
3	0	2	5
4	2	1	6
 

输入：receiver = [2,0,1], k = 4
输出：6
解释：上表展示了从编号为 x = 2 开始的游戏过程。
从表中可知，f(2) 等于 6 。
6 是能得到最大的函数值。
所以输出为 6 。
示例 2：

传递次数	传球者编号	接球者编号	x + 所有接球者编号
 	 	 	4
1	4	3	7
2	3	2	9
3	2	1	10
 

输入：receiver = [1,1,1,2,3], k = 3
输出：10
解释：上表展示了从编号为 x = 4 开始的游戏过程。
从表中可知，f(4) 等于 10 。
10 是能得到最大的函数值。
所以输出为 10 。
 

提示：

1 <= receiver.length == n <= 105
0 <= receiver[i] <= n - 1
1 <= k <= 1010
"""
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        ans = list(range(n))
        cur = list(range(n))
        f = receiver.copy()
        g = receiver.copy()
        i = 0
        while k:
            if (k >> i) & 1:
                for j in range(n):
                    ans[j] += g[cur[j]]
                c_cur = [0] * n
                for j in range(n):
                    c_cur[j] = f[cur[j]]
                cur = c_cur
                k -= 1 << i
            ff = [0] * n
            gg = [0] * n
            for j in range(n):
                ff[j] = f[f[j]]
                gg[j] = g[j] + g[f[j]]
            f = ff
            g = gg
            i += 1
        return max(ans)
