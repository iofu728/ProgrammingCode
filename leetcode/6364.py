# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-02-19 12:54:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-02-19 12:55:06

"""
6364. 无平方子集计数 显示英文描述 
通过的用户数52
尝试过的用户数161
用户总通过次数52
用户总提交次数223
题目难度Medium
给你一个正整数数组 nums 。

如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。

无平方因子数 是无法被除 1 之外任何平方数整除的数字。

返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 109 + 7 取余的结果。

nums 的 非空子集 是可以由删除 nums 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。

 

示例 1：

输入：nums = [3,4,4,5]
输出：3
解释：示例中有 3 个无平方子集：
- 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
- 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
- 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 3 个无平方子集。
示例 2：

输入：nums = [1]
输出：1
解释：示例中有 1 个无平方子集：
- 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 1 个无平方子集。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 30
"""
tmp = {1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30}
mod = 10**9 + 7


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = Counter(num for num in nums if num in tmp)
        note = Counter({1: 1})
        for v in cnt:
            if v != 1:
                new_note = Counter()
                for v1 in note:
                    new_note[v1] += note[v1]
                    if gcd(v, v1) == 1:
                        new_note[v1 * v] += note[v1] * cnt[v]
                    new_note[v1] %= mod
                note = new_note
        return (sum(note.values()) * pow(2, cnt[1], mod) - 1) % mod
