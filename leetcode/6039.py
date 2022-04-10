# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-10 23:54:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-10 23:54:23

"""
6039. K 次增加后的最大乘积 显示英文描述 
通过的用户数521
尝试过的用户数700
用户总通过次数522
用户总提交次数991
题目难度Medium
给你一个非负整数数组 nums 和一个整数 k 。每次操作，你可以选择 nums 中 任一 元素并将它 增加 1 。

请你返回 至多 k 次操作后，能得到的 nums的 最大乘积 。由于答案可能很大，请你将答案对 109 + 7 取余后返回。

 

示例 1：

输入：nums = [0,4], k = 5
输出：20
解释：将第一个数增加 5 次。
得到 nums = [5, 4] ，乘积为 5 * 4 = 20 。
可以证明 20 是能得到的最大乘积，所以我们返回 20 。
存在其他增加 nums 的方法，也能得到最大乘积。
示例 2：

输入：nums = [6,3,3,2], k = 2
输出：216
解释：将第二个数增加 1 次，将第四个数增加 1 次。
得到 nums = [6, 4, 3, 3] ，乘积为 6 * 4 * 3 * 3 = 216 。
可以证明 216 是能得到的最大乘积，所以我们返回 216 。
存在其他增加 nums 的方法，也能得到最大乘积。
 

提示：

1 <= nums.length, k <= 105
0 <= nums[i] <= 106
"""
class Solution:
    mods = 10 ** 9 + 7
    def maximumProduct(self, nums: List[int], k: int) -> int:
        N = len(nums)
        M = max(nums)
        s = sum(nums)
        if M * N - s <= k:
            x = M + (k + s - M * N) // N
            y = (k + s - M * N) % N
            return pow(x, N - y, self.mods) * pow(x + 1, y, self.mods) % self.mods
        c = Counter(nums)
        key = sorted(c.keys(), reverse=True)
        while k:
            a = key.pop()
            b = key.pop()
            if (b - a) * c[a] <= k:
                c[b] += c[a]
                k -= c[a] * (b - a)
                del c[a]
                key.append(b)
            else:
                # y = k // (b - a)
                x = c[a]

                base = a + k // x
                z = k % x
                c[a] = 0
                c[base] += x - z
                c[base + 1] += z
                # print(a, x, z, base, k)
                k = 0
            # print(c, key, k)
        res = 1
        # print(c)
        for ii, jj in c.items():
            if jj:
                res *= pow(ii, jj, self.mods)
        return res % self.mods
                
                
            