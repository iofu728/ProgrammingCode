# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-10 14:04:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-10 14:05:07

"""
6115. 统计理想数组的数目 显示英文描述 
通过的用户数19
尝试过的用户数64
用户总通过次数19
用户总提交次数83
题目难度Hard
给你两个整数 n 和 maxValue ，用于描述一个 理想数组 。

对于下标从 0 开始、长度为 n 的整数数组 arr ，如果满足以下条件，则认为该数组是一个 理想数组 ：

每个 arr[i] 都是从 1 到 maxValue 范围内的一个值，其中 0 <= i < n 。
每个 arr[i] 都可以被 arr[i - 1] 整除，其中 0 < i < n 。
返回长度为 n 的 不同 理想数组的数目。由于答案可能很大，返回对 109 + 7 取余的结果。

 

示例 1：

输入：n = 2, maxValue = 5
输出：10
解释：存在以下理想数组：
- 以 1 开头的数组（5 个）：[1,1]、[1,2]、[1,3]、[1,4]、[1,5]
- 以 2 开头的数组（2 个）：[2,2]、[2,4]
- 以 3 开头的数组（1 个）：[3,3]
- 以 4 开头的数组（1 个）：[4,4]
- 以 5 开头的数组（1 个）：[5,5]
共计 5 + 2 + 1 + 1 + 1 = 10 个不同理想数组。
示例 2：

输入：n = 5, maxValue = 3
输出：11
解释：存在以下理想数组：
- 以 1 开头的数组（9 个）：
   - 不含其他不同值（1 个）：[1,1,1,1,1] 
   - 含一个不同值 2（4 个）：[1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - 含一个不同值 3（4 个）：[1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- 以 2 开头的数组（1 个）：[2,2,2,2,2]
- 以 3 开头的数组（1 个）：[3,3,3,3,3]
共计 9 + 1 + 1 = 11 个不同理想数组。
 

提示：

2 <= n <= 104
1 <= maxValue <= 104
"""


class Solution:
    MODS = 10 ** 9 + 7

    def idealArrays(self, n: int, maxValue: int) -> int:
        @lru_cache(None)
        def getFactor(n):
            if n == 1:
                return defaultdict(int)
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    tmp = deepcopy(getFactor(n // i))
                    tmp[i] += 1
                    return tmp
            tmp = defaultdict(int)
            tmp[n] = 1
            return tmp

        @lru_cache(None)
        def getcomb(m, n):
            return comb(m, n) % self.MODS

        res = 0
        for ii in range(1, maxValue + 1):
            x = 1
            for m in getFactor(ii).values():
                x = (x * getcomb(n + m - 1, n - 1)) % self.MODS
            res = (res + x) % self.MODS
        return res
