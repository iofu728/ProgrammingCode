# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-10 13:11:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-10 13:11:52

"""
5897. 将数组分成两个数组并最小化数组和的差 显示英文描述 
通过的用户数140
尝试过的用户数653
用户总通过次数160
用户总提交次数1707
题目难度Hard
给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。nums 中每个元素都需要放入两个数组之一。

请你返回 最小 的数组和之差。

 

示例 1：

example-1

输入：nums = [3,9,7,3]
输出：2
解释：最优分组方案是分成 [3,9] 和 [7,3] 。
数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
示例 2：

输入：nums = [-36,36]
输出：72
解释：最优分组方案是分成 [-36] 和 [36] 。
数组和之差的绝对值为 abs((-36) - (36)) = 72 。
示例 3：

example-3

输入：nums = [2,-1,0,4,-2,-9]
输出：0
解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。
 

提示：

1 <= n <= 15
nums.length == 2 * n
-107 <= nums[i] <= 107
"""


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def picker(a):
            res, d = [[]], defaultdict(set)
            for ii in a:
                res += [jj + [ii] for jj in res]
            for ii in res:
                d[len(ii)].add(sum(ii))
            return d

        N = len(nums)
        s = sum(nums)
        n = N // 2
        a, b = picker(nums[:n]), picker(nums[n:])
        res = float("inf")
        for ii in range(n + 1):
            x = sorted(b[n - ii])
            for kk in a[ii]:
                idx = bisect.bisect_left(x, s // 2 - kk)
                res = min(res, abs(s - 2 * (kk + x[min(len(x) - 1, idx)])))
        return res
