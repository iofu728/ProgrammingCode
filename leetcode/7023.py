# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-13 11:20:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-13 11:20:40

"""
7023. 操作使得分最大 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数2
题目难度Hard
给你一个长度为 n 的正整数数组 nums 和一个整数 k 。

一开始，你的分数为 1 。你可以进行以下操作至多 k 次，目标是使你的分数最大：

选择一个之前没有选过的 非空 子数组 nums[l, ..., r] 。
从 nums[l, ..., r] 里面选择一个 质数分数 最高的元素 x 。如果多个元素质数分数相同且最高，选择下标最小的一个。
将你的分数乘以 x 。
nums[l, ..., r] 表示 nums 中起始下标为 l ，结束下标为 r 的子数组，两个端点都包含。

一个整数的 质数分数 等于 x 不同质因子的数目。比方说， 300 的质数分数为 3 ，因为 300 = 2 * 2 * 3 * 5 * 5 。

请你返回进行至多 k 次操作后，可以得到的 最大分数 。

由于答案可能很大，请你将结果对 109 + 7 取余后返回。

 

示例 1：

输入：nums = [8,3,9,3,8], k = 2
输出：81
解释：进行以下操作可以得到分数 81 ：
- 选择子数组 nums[2, ..., 2] 。nums[2] 是子数组中唯一的元素。所以我们将分数乘以 nums[2] ，分数变为 1 * 9 = 9 。
- 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 1 ，但是 nums[2] 下标更小。所以我们将分数乘以 nums[2] ，分数变为 9 * 9 = 81 。
81 是可以得到的最高得分。
示例 2：

输入：nums = [19,12,14,6,10,18], k = 3
输出：4788
解释：进行以下操作可以得到分数 4788 ：
- 选择子数组 nums[0, ..., 0] 。nums[0] 是子数组中唯一的元素。所以我们将分数乘以 nums[0] ，分数变为 1 * 19 = 19 。
- 选择子数组 nums[5, ..., 5] 。nums[5] 是子数组中唯一的元素。所以我们将分数乘以 nums[5] ，分数变为 19 * 18 = 342 。
- 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 2，但是 nums[2] 下标更小。所以我们将分数乘以 nums[2] ，分数变为  342 * 14 = 4788 。
4788 是可以得到的最高的分。
 

提示：

1 <= nums.length == n <= 105
1 <= nums[i] <= 105
1 <= k <= min(n * (n + 1) / 2, 109)
"""

Y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
class Solution:
    MODS = 10 ** 9 + 7
    def maximumScore(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def get_num(x):
            res = 0
            for ii in Y:
                flag = True
                while x % ii == 0:
                    if flag:
                        res += 1
                    x //= ii
                    flag = False
            if x != 1:
                res += 1
            return res
        N = len(nums)
        y = [get_num(ii) for ii in nums]
        r = [N] * N
        l = [-1] * N
        q = []
        for ii in range(N):
            now = y[ii]
            while q and q[-1][0] < now:
                pre = q.pop()
                r[pre[1]] = ii
            q.append((now, ii))
        q = []
        for ii in range(N):
            now = y[ii]
            while q and q[-1][0] < now:
                pre = q.pop()
                r[pre[1]] = ii
            if q:
                l[ii] = q[-1][1]
            q.append((now, ii))
        # print(y, l, r)
        res = 1
        for idx, now in sorted(enumerate(nums), key=lambda i:(-i[1])):
            r_idx = r[idx]
            l_idx = l[idx]
            t = r_idx - idx + (idx - l_idx - 1) * (r_idx - idx)
            # print(k, t, idx, now)
            if t >= k:
                res = (res * pow(now, k, self.MODS)) % self.MODS
                break
            res = (res * pow(now, t, self.MODS)) % self.MODS
            k -= t
        return res