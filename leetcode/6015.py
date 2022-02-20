# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-20 11:33:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-20 11:33:43

"""
6015. 统计可以被 K 整除的下标对数目 显示英文描述 
通过的用户数78
尝试过的用户数329
用户总通过次数79
用户总提交次数464
题目难度Hard
给你一个下标从 0 开始、长度为 n 的整数数组 nums 和一个整数 k ，返回满足下述条件的下标对 (i, j) 的数目：

0 <= i < j <= n - 1 且
nums[i] * nums[j] 能被 k 整除。
 

示例 1：

输入：nums = [1,2,3,4,5], k = 2
输出：7
解释：
共有 7 对下标的对应积可以被 2 整除：
(0, 1)、(0, 3)、(1, 2)、(1, 3)、(1, 4)、(2, 3) 和 (3, 4)
它们的积分别是 2、4、6、8、10、12 和 20 。
其他下标对，例如 (0, 2) 和 (2, 4) 的乘积分别是 3 和 15 ，都无法被 2 整除。    
示例 2：

输入：nums = [1,2,3,4], k = 5
输出：0
解释：不存在对应积可以被 5 整除的下标对。
 

提示：

1 <= nums.length <= 105
1 <= nums[i], k <= 105
"""


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def gcd(a, b):
            return math.gcd(a, b)

        N = len(nums)
        g = defaultdict(int)
        for ii in nums:
            t = gcd(ii, k)
            g[t] += 1
        m = defaultdict(list)
        g_k = sorted(g.keys(), reverse=True)
        for ii in range(len(g)):
            kk = k // g_k[ii]
            for jj in range(ii, len(g)):
                if g_k[jj] % kk == 0:
                    m[g_k[ii]].append(g_k[jj])

        res = 0
        # print(g)
        # print(m)
        for ii, jj in g.items():
            for kk in m[ii]:
                if kk == ii:
                    res += jj * (jj - 1) // 2
                else:
                    res += jj * g[kk]
        return res