# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-09-04 11:21:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-09-04 11:21:58

"""
6169. 最长优雅子数组 显示英文描述 
通过的用户数5
尝试过的用户数6
用户总通过次数5
用户总提交次数6
题目难度Medium
给你一个由 正 整数组成的数组 nums 。

如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。

返回 最长 的优雅子数组的长度。

子数组 是数组中的一个 连续 部分。

注意：长度为 1 的子数组始终视作优雅子数组。

 

示例 1：

输入：nums = [1,3,8,48,10]
输出：3
解释：最长的优雅子数组是 [3,8,48] 。子数组满足题目条件：
- 3 AND 8 = 0
- 3 AND 48 = 0
- 8 AND 48 = 0
可以证明不存在更长的优雅子数组，所以返回 3 。
示例 2：

输入：nums = [3,1,5,11,13]
输出：1
解释：最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        @lru_cache(None)
        def is_ok(x, y):
            return (x & y) == 0

        N = len(nums)
        res = 0
        for l in range(N):
            r = l
            check_set = set([nums[l]])
            while r + 1 < N and all(is_ok(jj, nums[r + 1]) for jj in check_set):
                r += 1
                check_set.add(nums[r])
            res = max(res, r - l + 1)
        return res
            